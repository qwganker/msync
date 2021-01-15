import json

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.WebCookie import WebCookie
from common.Timeutils import TimeUtils

import logging

logger = logging.getLogger('log')


class JianshuDriver(BaseSiteDriver):
    def __init__(self):
        super().__init__()
        self.__cookies = WebCookie().getAllCookies()

    def __fetchBlogCategoryList(self):
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        url = 'https://www.jianshu.com/author/notebooks'
        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        if response.status_code != 200:
            return False, ''

        return True, response.text

    def fetchBlogCategoryList(self, param=None):
        success, data = self.__fetchBlogCategoryList()

        if not success:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=data)

    def fetchBlogList(self, param=None):
        url = "https://www.jianshu.com/author/notebooks/" + str(param['id']) + "/notes"
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def fetchContentBlog(self, param=None):
        url = "https://www.jianshu.com/author/notes/" + str(param["id"]) + "/content"
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "max-age=0",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def __saveUpdate(self, param):
        url = "https://www.jianshu.com/author/notes/" + str(param["id"])
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": str(len(param["content"])),
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }

        payload = {"id": str(param["id"]), "autosave_control": param['autosave_control'], "title": param['title'],
                   "content": param['content']}

        response = HttpRequestUtil.put(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        if response.status_code != 200:
            return False

        return True

    def publishUpdateBlog(self, param):

        # 先保存更新内容
        if not self.__saveUpdate(param):
            return HttpResult.error(info="更新发布失败")

        # 发布更新
        url = "https://www.jianshu.com/author/notes/" + str(param['id']) + "/publicize"
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

        payload = {}
        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 'error' in result:
            return HttpResult.error(info=result['error'][0]['message'])

        return HttpResult.ok(info="更新发布成功", data=result)

    def __createDefaultNewBlog(self, cateId):
        payload = {"notebook_id": cateId, "title": TimeUtils.getNowDate(), "at_bottom": True}

        url = 'https://www.jianshu.com/author/notes'
        headers = {
            "Host": "www.jianshu.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": str(payload),
            "Origin": "https://www.jianshu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.jianshu.com/writer",
        }
        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        if response.status_code != 200:
            return False, ''

        return True, response.text

    def publishNewBlog(self, param):
        success, cateList = self.__fetchBlogCategoryList()

        if not success:
            return HttpResult.error(info="发布失败")

        cateListData = json.loads(cateList)
        firstCateId = cateListData[0]['id']

        success, result = self.__createDefaultNewBlog(firstCateId)
        if not success:
            return HttpResult.error(info='发布失败')

        newBlog = json.loads(result)

        param = {"id": str(newBlog['id']), "autosave_control": 1, "title": param['title'], "content": param['content']}

        success, self.publishUpdateBlog(param)
        if not success:
            return HttpResult.error(info='发布失败')

        return HttpResult.ok(info='发布成功')

    def deleteBlog(self, param):

        url = "https://www.jianshu.com/author/notes/" + str(param['id']) + "/soft_destroy"
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

        payload = {}

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        if response.status_code != 200:
            return HttpResult.error(info="删除失败")

        result = json.loads(response.text)
        return HttpResult.ok(info="删除成功", data=result)
