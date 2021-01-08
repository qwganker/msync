from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
import browser_cookie3
import requests
import json
from common.HttpResult import HttpResult
from common.HttpRequestUtil import HttpRequestUtil
from common.platformdriver import PlatformDriver
from common.Timeutils import TimeUtils

class JianshuDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = PlatformDriver.getCookies()

    def publishNewBlog(self, param):
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",

            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "71",
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        # 先创建
        url = "https://www.jianshu.com/author/notes"
        payload={"at_bottom":True,"notebook_id":7,"title":"test-02-01","title":TimeUtils.getNow()}

        # 再发布

        return HttpResult.ok(info="发布成功")

    def fetchBlogCate(self, param=None):

        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control":"max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        url = 'https://www.jianshu.com/author/notebooks'
        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def fetchBlogListInCate(self, param=None):
        url = "https://www.jianshu.com/author/notebooks/"+str(param['id'])+"/notes"
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control":"max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def fetchBlogContent(self, param=None):
        url = "https://www.jianshu.com/author/notes/"+str(param["id"])+"/content"
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control":"max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def updateBlogContent(self, param):
        url = "https://www.jianshu.com/author/notes/" + str(param["id"])
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": str(len(param["text"])),
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        payload={"id":str(param["id"]), "autosave_control": param['autosave_control'], "title":param['title'], "content":param['text']}

        response = HttpRequestUtil.put(url, headers=headers, data=json.dumps(payload), cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="更新失败")

        return HttpResult.ok(info="更新成功", data=response.text)

    def publishBlog(self, param):

        url = "https://www.jianshu.com/author/notes/"+ str(param['id']) +"/publicize"

        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": str(2),
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        payload={}

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookie)
        result = json.loads(response.text)
        if 'error' in result:
            return HttpResult.error(info=result['error'][0]['message'])

        return HttpResult.ok(info="发布成功", data=result)

    def deleteBlog(self, param):

        url = "https://www.jianshu.com/author/notes/"+str(param['id'])+"/soft_destroy"
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": str(2),
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        payload={}

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="删除失败")
        
        result = json.loads(response.text)
        return HttpResult.ok(info="删除成功", data=result)
