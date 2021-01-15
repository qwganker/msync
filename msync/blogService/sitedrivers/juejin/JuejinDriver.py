import json

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.WebCookie import WebCookie
from common.Timeutils import TimeUtils

import logging

logger = logging.getLogger('log')


class JuejinDriver(BaseSiteDriver):
    def __init__(self):
        super().__init__()
        self.__cookies = WebCookie().getAllCookies()

    def fetchBlogCategoryList(self, param=None):
        """
        获取博客分类
        """
        pass

    def __getUserInfo(self):
        url = 'https://api.juejin.cn/user_api/v1/user/get?aid=2608&not_self=0'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'api.juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/',
            'TE': 'Trailers',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookies)
        return json.loads(response.text)

    def fetchBlogList(self, param=None):
        """
        获取某一个分类下的文章列表
        """

        url = 'https://api.juejin.cn/content_api/v1/article/query_list'

        userInfo = self.__getUserInfo()
        if 0 != userInfo['err_no']:
            return HttpResult.error(info="获取失败")

        userId = userInfo['data']['user_id']

        payload = {"user_id": userId, "sort_type": 2, "cursor": "0"}
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': str(len(payload)),
            'Content-Type': 'application/json',
            'Host': 'api.juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/user/' + userId + '/post',
            'TE': 'Trailers',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 0 != result['err_no']:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=result['data'])

    def fetchContentBlog(self, param=None):
        url = 'https://api.juejin.cn/content_api/v1/article/detail'

        article_id = param['id']
        payload = {"article_id": article_id}

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': str(len(payload)),
            'Content-Type': 'application/json',
            'Host': 'api.juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/post/' + article_id,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 0 != result['err_no']:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=result['data'])

    def publishUpdateBlog(self, param):
        """
        更新
        """
        pass

    def publishNewBlog(self, param):
        """
        发布
        """
        pass

    def deleteBlog(self, param):
        """
        删除
        """
        pass
