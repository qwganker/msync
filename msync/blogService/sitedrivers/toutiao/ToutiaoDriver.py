import time

import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.WebDriver import WebDriver
from common.WebCookie import WebCookie
from common.StringUtil import StringUtil

import logging

logger = logging.getLogger('log')


class ToutiaoDriver(BaseSiteDriver):
    def __init__(self):
        super().__init__()
        self.__cookies = WebCookie().getAllCookies()

    def __setDriverCookie(self, driver):
        for c in self.__cookies:
            if 'toutiao.com' in c.domain:
                isScure = True
                if c.secure == 0:
                    isScure = False
                driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'secure': isScure})

    def fetchBlogCategoryList(self, param=None):
        pass

    def fetchBlogList(self, param=None):
        # url = 'https://mp.toutiao.com/mp/agw/creator_center/list?type=2&status=0&start_cursor=0&end_cursor=0&size=10&mode=2&need_stat=true&page_time={"index":1,"time_stamp":0}&filter_params={"search_word":"","source":0}&app_id=1231'
        url = 'https://mp.toutiao.com/mp/agw/creator_center/list?'

        headers = {
            "Host": "mp.toutiao.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
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
        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def fetchContentBlog(self, param=None):

        aid = str(param['id'])

        url = "https://mp.toutiao.com/mp/agw/article/edit?pgc_id=" + aid + "&format=json"
        headers = {
            "Host": "mp.toutiao.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Referer": "https://mp.toutiao.com/profile_v4/graphic/publish?pgc_id=" + aid
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def publishUpdateBlog(self, param):
        url = "https://mp.toutiao.com/profile_v4/graphic/publish?pgc_id=" + param['id']

        webDriver = WebDriver.getDriver()

        webDriver.maximize_window()

        # 必须先打开才能添加cookie
        webDriver.get(url)
        self.__setDriverCookie(webDriver)
        webDriver.get(url)

        # 设置title
        try:
            title_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea'
            WebDriverWait(webDriver, 20, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, title_xpath)))
            title = webDriver.find_element_by_xpath(title_xpath)
            title.clear()
            title.send_keys(param['title'])

            # 设置内容
            webDriver.execute_script(
                "document.getElementsByClassName('ProseMirror')[0].innerHTML='" + StringUtil.removeBlankAndBreakLine(param['content']) + "'")

            time.sleep(1)

            # 点击发布按钮
            publishBtn_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[3]/div/button'
            WebDriverWait(webDriver, 20, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, publishBtn_xpath)))
            publishBtn = webDriver.find_element_by_xpath(publishBtn_xpath)
            publishBtn.click()
        except Exception as e:
            logger.warning(e)
        finally:
            time.sleep(5)
            webDriver.close()
            return HttpResult.ok(info="更新成功")

    def publishNewBlog(self, param):
        url = 'https://mp.toutiao.com/profile_v4/graphic/publish'

        webDriver = WebDriver.getDriver()
        webDriver.maximize_window()

        # 必须先打开才能添加cookie
        webDriver.get(url)
        self.__setDriverCookie(webDriver)
        webDriver.get(url)

        try:
            title_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea'
            WebDriverWait(webDriver, 20, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, title_xpath)))
            title = webDriver.find_element_by_xpath(title_xpath)
            title.clear()
            title.send_keys(param['title'])

            # 设置内容
            content = StringUtil.removeBlankAndBreakLine(param['content'])
            logger.warning(content)
            js = "document.getElementsByClassName('ProseMirror')[0].innerHTML = '" + content + "'"
            logger.warning(js)
            webDriver.execute_script(js)

            # 设置无图
            coverBtn_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/label[3]/span/div'
            WebDriverWait(webDriver, 20, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, coverBtn_xpath)))
            coverBtn = webDriver.find_element_by_xpath(coverBtn_xpath)
            coverBtn.click()

            # 点击发布按钮
            publishBtn_xpath = '/html/body/div[1]/div/div[3]/section/main/div[2]/div/div/div[3]/div/button[4]'
            WebDriverWait(webDriver, 20, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, publishBtn_xpath)))
            publishBtn = webDriver.find_element_by_xpath(publishBtn_xpath)
            publishBtn.click()

        except Exception as e:
            logger.warning(e)
        finally:
            time.sleep(5)
            webDriver.close()
            return HttpResult.ok(info="发布成功")

    def deleteBlog(self, param):
        url = 'https://mp.toutiao.com/mp/agw/article/delete/'

        blog_attr = param['blog']['article_attr']

        logger.info(blog_attr)

        item_id = str(blog_attr['item_id'])
        mp_id = str(blog_attr['mp_id'])
        create_time = str(blog_attr['create_time'])
        article_type = str(blog_attr['type'])

        pgc_cell = json.loads(blog_attr['pgc_cell'])
        group_source = str(pgc_cell['group_source'])
        has_article_pgc = str(pgc_cell['has_article_pgc'])

        payload = 'item_id=' + item_id \
                  + '&pgc_id=' + item_id \
                  + '&id=' + item_id \
                  + '&article_type=' + article_type \
                  + '&group_id=' + item_id \
                  + '&source_type=0&has_article_pgc=' + has_article_pgc \
                  + '&book_id=&create_time=' + create_time \
                  + '&group_source=' + group_source \
                  + '&mp_id=' + mp_id

        headers = {
            "Host": "mp.toutiao.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Content-Length": str(len(payload)),
            "Origin": "https://mp.toutiao.com",
            "Referer": "https://mp.toutiao.com/profile_v4/graphic/articles",
            "Connection": "keep-alive",
            "TE": "Trailers"
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="删除失败")

        return HttpResult.ok(info="删除成功")
