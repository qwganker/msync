from blogService.drivers.BaseSiteDriver import BaseSiteDriver
import browser_cookie3
import requests
import json
import gzip
from common.HttpResult import HttpResult
from common.HttpRequestUtil import HttpRequestUtil

class ToutiaoDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = browser_cookie3.firefox()

    def fetchBlogCate(self, param=None):
        pass

    def fetchBlogListInCate(self, param=None):
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


    def fetchBlogContent(self, param=None):

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


    def updateBlogContent(self, param):
        pass

    def publishBlog(self, param):
        pass

    def deleteBlog(self, param):
        pass
