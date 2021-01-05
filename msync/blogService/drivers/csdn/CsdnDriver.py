from blogService.drivers.BaseSiteDriver import BaseSiteDriver
import browser_cookie3
import requests
import json
from common.HttpResult import HttpResult
from urllib.parse import urlparse
from base64 import b64decode,b64encode
import hashlib
import hmac
import random
import http.cookiejar as cookielib

class CsdnDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = browser_cookie3.firefox()

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

    def createSign(self, uuid, url):
        s = urlparse(url)
        ekey = "9znpamsyl2c7cdrr9sas0le9vbc3r6ba".encode()
        to_enc = f"GET\napplication/json, text/plain, */*\n\n\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{s.path+'?'+s.query}".encode()
        sign = b64encode(hmac.new(ekey, to_enc, digestmod=hashlib.sha256).digest()).decode()
        return sign

    def fetchBlogCate(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/list?type=all"

        uuid = self.createUuid()
        sign = self.createSign(uuid, url)

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
 
        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        result = json.loads(response.text)

        return HttpResult.ok(info="获取成功", data=result['data'])

    def fetchBlogListInCate(self, param=None):
        url = "https://bizapi.csdn.net/blog-console-api/v1/column/getAllArticles?column_id="+str(param['id'])


        uuid = self.createUuid()
        sign = self.createSign(uuid, url)

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
 
        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        if response.status_code != 200:
            return HttpResult.error(info="获取失败")

        result = json.loads(response.text)

        return HttpResult.ok(info="获取成功", data=result['data'])

    def fetchBlogContent(self, param=None):

        aid = str(param['id'])

        url="https://bizapi.csdn.net/blog-console-api/v3/editor/getArticle?id="+aid+"&model_type"

        uuid = self.createUuid()
        sign = self.createSign(uuid, url)

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
        # print(url)

        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        # print(response.status_code)
        # print(response.headers)
        # print(response.text)
        return HttpResult.ok(info="获取成功", data=response.text)

    def updateBlogContent(self, param):
        pass

    def publishBlog(self, param):
        pass

    def deleteBlog(self, param):
        pass
