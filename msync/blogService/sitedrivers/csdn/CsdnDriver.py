from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver
import browser_cookie3
import requests
import json
from common.HttpResult import HttpResult
from common.HttpRequestUtil import HttpRequestUtil
from urllib.parse import urlparse
from base64 import b64decode,b64encode
import hashlib
import hmac
import random
import http.cookiejar as cookielib
from common.platformdriver import PlatformDriver

class CsdnDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = PlatformDriver.getCookies()

    def createUuid(self):
        text = ""
        char_list = []
        for c in range(97,97+6):
            char_list.append(chr(c))
        for c in range(49,58):
            char_list.append(chr(c))
        for i in "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx":
            if i == "4":
                text += "4"
            elif i == "-":
                text += "-"
            else:
                text += random.choice(char_list)
        return text

    def createSign(self, method, uuid, url):
        uri = urlparse(url)
        ekey = "9znpamsyl2c7cdrr9sas0le9vbc3r6ba".encode()

        if method == 'GET':
            to_enc = f"{method}\napplication/json, text/plain, */*\n\n\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{uri.path+'?'+uri.query}".encode()
        else:
            to_enc = f"{method}\napplication/json, text/plain, */*\n\napplication/json\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{uri.path}".encode()

        print(to_enc)

        sign = b64encode(hmac.new(ekey, to_enc, digestmod=hashlib.sha256).digest()).decode()
        return sign

    def fetchBlogCate(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/list?type=all"

        uuid = self.createUuid()
        sign = self.createSign("GET", uuid, url)

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

    def fetchBlogListInCate(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/getAllArticles?column_id="+str(param['id'])


        uuid = self.createUuid()
        sign = self.createSign('GET', uuid, url)

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

    def fetchBlogContent(self, param=None):

        aid = str(param['id'])

        url="https://bizapi.csdn.net/blog-console-api/v3/editor/getArticle?id="+aid+"&model_type"

        uuid = self.createUuid()
        sign = self.createSign('GET', uuid, url)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://editor.csdn.net/md/?articleId="+aid,
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

    def updateBlogContent(self, param):
        aid = str(param['data']['id'])

        url = "https://bizapi.csdn.net/blog-console-api/v3/mdeditor/saveArticle"
        uuid = self.createUuid()
        sign = self.createSign('POST', uuid, url)

        headers = {
            "Host": "bizapi.csdn.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://editor.csdn.net/md/?articleId="+aid,
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

    def publishBlog(self, param):


        pass

    def deleteBlog(self, param):
        pass
