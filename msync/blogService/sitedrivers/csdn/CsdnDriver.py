import hashlib
import hmac
import json
import random
from base64 import b64encode
from urllib.parse import urlparse

from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
from common.HttpRequestUtil import HttpRequestUtil
from common.HttpResult import HttpResult
from common.platformdriver import PlatformDriver

import logging

logger = logging.getLogger('log')


class CsdnDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__cookie = PlatformDriver.getCookies()

    def __createUUID(self):
        text = ""
        char_list = []
        for c in range(97, 97 + 6):
            char_list.append(chr(c))
        for c in range(49, 58):
            char_list.append(chr(c))
        for i in "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx":
            if i == "4":
                text += "4"
            elif i == "-":
                text += "-"
            else:
                text += random.choice(char_list)
        return text

    def __httpPostSign(self, caSignStr):
        ekey = "9znpamsyl2c7cdrr9sas0le9vbc3r6ba".encode()

        logger.info("[cd sign]:%s\n", caSignStr)

        sign = b64encode(hmac.new(ekey, caSignStr, digestmod=hashlib.sha256).digest()).decode()
        return sign


    def __httpGetSign(self, uuid, url):
        uri = urlparse(url)
        ekey = "9znpamsyl2c7cdrr9sas0le9vbc3r6ba".encode()

        to_enc = f"GET\napplication/json, text/plain, */*\n\n\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{uri.path + '?' + uri.query}".encode()

        logger.info("[sign]:%s\n",to_enc)

        sign = b64encode(hmac.new(ekey, to_enc, digestmod=hashlib.sha256).digest()).decode()
        return sign

    def fetchBlogCategoryList(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/list?type=all"

        uuid = self.__createUUID()
        sign = self.__httpGetSign(uuid, url)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://mp.csdn.net/console/column/allColumnList",
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://mp.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers"
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        result = json.loads(response.text)

        return HttpResult.ok(info="获取成功", data=result['data'])

    def fetchBlogList(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/getAllArticles?column_id=" + str(param['id'])

        uuid = self.__createUUID()
        sign = self.__httpGetSign(uuid, url)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://mp.csdn.net/console/column/allColumnList",
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://mp.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers"
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        result = json.loads(response.text)

        return HttpResult.ok(info="获取成功", data=result['data'])

    def fetchContentBlog(self, param=None):

        aid = str(param['id'])

        url = "https://bizapi.csdn.net/blog-console-api/v3/editor/getArticle?id=" + aid + "&model_type"

        uuid = self.__createUUID()
        sign = self.__httpGetSign(uuid, url)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://editor.csdn.net/md/?articleId=" + aid,
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://editor.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers",
            "Cache-Control": "max-age=0"
        }

        response = HttpRequestUtil.get(url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        return HttpResult.ok(info="获取成功", data=response.text)

    def publishUpdateBlog(self, param):
        aid = str(param['data']['id'])

        url = "https://bizapi.csdn.net/blog-console-api/v3/mdeditor/saveArticle"

        uuid = self.__createUUID()
        uri = urlparse(url)
        caSignStr = f"POST\napplication/json, text/plain, */*\n\napplication/json\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{uri.path}".encode()
        sign = self.__httpPostSign(caSignStr)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://editor.csdn.net/md/?articleId=" + aid,
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://editor.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers",
            "Cache-Control": "max-age=0",
            "Content-Type": "application/json",
            "Content-Length": str(len(param['data']))
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(param['data']), cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="更新失败")

        return HttpResult.ok(info="更新成功", data=response.text)

    def publishNewBlog(self, param):
        url = "	https://bizapi.csdn.net/blog-console-api/v3/mdeditor/saveArticle"
        uuid = self.__createUUID()
        caSignStr = f"POST\n*/*\n\napplication/json\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n/blog-console-api/v3/mdeditor/saveArticle".encode()
        sign = self.__httpPostSign(caSignStr)

        payload = {"title": str(param['title']), "markdowncontent": str(param['content']),
                   "content": str(param['content']), "readType": "public", "tags": "", "status": 0,
                   "categories": str(param['cate']), "type": "original", "original_link": "", "authorized_status": False,
                   "not_auto_saved": "1", "source": "pc_mdeditor"}
        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": 'https://editor.csdn.net/md/',
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://editor.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers",
            "Content-Type": "application/json",
            "Content-Length": str(len(payload))
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="发布失败")

        return HttpResult.ok(info="发布成功", data=response.text)

    def deleteBlog(self, param):
        url = 'https://bizapi.csdn.net/blog-console-api/v1/article/del'

        uuid = self.__createUUID()
        uri = urlparse(url)
        caSignStr = f"POST\napplication/json, text/plain, */*\n\napplication/json\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{uri.path}".encode()

        sign = self.__httpPostSign(caSignStr)

        payload = {"article_id": str(param['id']), "deep": "false"}
        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": 'https://mp.csdn.net/console/article',
            "X-Ca-Key": "203803574",
            "X-Ca-Nonce": uuid,
            "X-Ca-Signature": sign,
            "X-Ca-Signature-Headers": "x-ca-key,x-ca-nonce",
            "Origin": "https://editor.csdn.net",
            "Connection": "keep-alive",
            "TE": "Trailers",
            "Cache-Control": "max-age=0",
            "Content-Type": "application/json",
            "Content-Length": str(len(payload))
        }

        response = HttpRequestUtil.post(url, headers=headers, data=json.dumps(payload), cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="删除失败")

        return HttpResult.ok(info="删除成功", data=response.text)
