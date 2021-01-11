import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.platformdriver import PlatformDriver


class ToutiaoDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__cookie = PlatformDriver.getCookies()

    def __setDriverCookie(self, driver):
        for c in self.__cookie:
            if 'toutiao.com' in c.domain:
                isScure = True
                if (c.secure == 0):
                    isScure = False
                driver.add_cookie({'name' : c.name, 'value' : c.value, 'path' : c.path, 'secure': isScure})

    def fetchBlogCategoryList(self, param=None):
        pass

    def fetchBlogList(self, param=None):
        url = 'https://mp.toutiao.com/mp/agw/creator_center/list?type=2&status=0&start_cursor=0&end_cursor=0&size=10&mode=2&need_stat=true&page_time={"index":1,"time_stamp":0}&filter_params={"search_word":"","source":0}&app_id=1231'

        headers = {
            "Host": "mp.toutiao.com",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Referer": "https://mp.toutiao.com/profile_v4/graphic/articles"
        }

        '''
        response.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩 类型：bytes
        reponse.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码。类型：str
        '''
        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def fetchContentBlog(self, param=None):

        aid = str(param['id'])

        url = "https://mp.toutiao.com/mp/agw/article/edit?pgc_id="+aid+"&format=json"
        headers = {
            "Host": "mp.toutiao.com",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Referer": "https://mp.toutiao.com/profile_v4/graphic/publish?pgc_id="+aid
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def publishUpdateBlog(self, param):
        url = "https://mp.toutiao.com/profile_v4/graphic/publish?pgc_id="+ param['id']

        driver = PlatformDriver.getDriver()
        driver.maximize_window()

        # 必须先打开才能添加cookie
        driver.get(url)

        self.__setDriverCookie(driver)

        driver.get(url)

        # 设置title
        try:

            title_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea'
            WebDriverWait(driver, 20, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, title_xpath)))
            title = driver.find_element_by_xpath(title_xpath)
            title.clear()
            title.send_keys(param['title'])

            # 设置内容
            driver.execute_script("document.getElementsByClassName('ProseMirror')[0].innerHTML='"+param['content']+"'")

            # 点击发布按钮
            publishBtn_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[3]/div/button'
            WebDriverWait(driver, 20, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, publishBtn_xpath)))
            publishBtn = driver.find_element_by_xpath(publishBtn_xpath)
            publishBtn.click()

        finally:
            time.sleep(10)
            driver.close()
            return HttpResult.ok(info="更新成功")

    def publishNewBlog(self, param):
        pass

    def deleteBlog(self, param):
        pass
