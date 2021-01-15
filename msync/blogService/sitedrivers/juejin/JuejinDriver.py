import json

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.WebCookie import WebCookie

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

    def __updateArticleDraft(self, param):
        url = 'https://juejin.cn/content_api/v1/article_draft/update'

        draft_id = param['meta']['blog']['article_info']['draft_id']
        category_id = param['meta']['blog']['category']['category_id']
        tag_ids = []
        for tag in param['meta']['blog']['tags']:
            tag_ids.append(tag['tag_id'])

        title = param['title']

        payload = {"id": draft_id, "category_id": category_id, "tag_ids": tag_ids,
                   "link_url": "", "cover_image": "", "is_gfw": 0, "title": title, "brief_content": "", "is_english": 0,
                   "is_original": 1, "edit_type": 10, "html_content": "deprecated",
                   "mark_content": param['content']}

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Content-Length': str(len(str(payload))),
            'Host': 'juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/editor/drafts/' + draft_id,
            'TE': 'Trailers',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 0 != result['err_no']:
            return False, "草稿保存失败"

        return True, result['data']

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
        success, data = self.__updateArticleDraft(param)
        if False == success:
            return HttpResult.error(info=data)

        article_id = data['id']

        url = 'https://juejin.cn/content_api/v1/article/publish'
        payload = {"draft_id": article_id}
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Content-Length': str(len(payload)),
            'Host': 'api.juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/editor/drafts/' + article_id,
            'TE': 'Trailers',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 0 != result['err_no']:
            return HttpResult.error(info="发布更新失败")

        return HttpResult.ok(info="发布更新成功", data=result['data'])

    def publishNewBlog(self, param):
        """
        发布
        """
        pass

    def deleteBlog(self, param):
        """
        删除
        """

        url = 'https://api.juejin.cn/content_api/v1/article/delete'
        article_id = param['id']
        payload = {"article_id": article_id}
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Content-Length': str(len(payload)),
            'Host': 'api.juejin.cn',
            'Origin': 'https://juejin.cn',
            'Referer': 'https://juejin.cn/user/' + article_id + '/posts',
            'TE': 'Trailers',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookies)
        result = json.loads(response.text)
        if 0 != result['err_no']:
            return HttpResult.error(info="删除失败")

        return HttpResult.ok(info="删除成功")
