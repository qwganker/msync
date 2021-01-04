from blogService.drivers.BaseSiteDriver import BaseSiteDriver
import browser_cookie3
import requests

class JianshuDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = browser_cookie3.firefox()

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


    def add(self, param):
        
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

        # # 判断是否登录
        # url = "https://www.jianshu.com/author/notes/82101346"

        # payload={"id":"82101346","autosave_control":7,"title":"test-02-01","content":reqParam['text']}


        # cookie = {}

        # response = requests.request("PUT", url, headers=headers, data=json.dumps(payload), cookies=cj)
        # print(response.text)

        # # 执行操作
        pass

    def update(self, param):
        pass

    def fetchBlogCategory(self, param=None):

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
        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        return response.text
    
    def fetchBlogList(self, param=None):
        url = "https://www.jianshu.com/author/notebooks/"+str(param)+"/notes"
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

        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        return response.text

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

        response = requests.request("GET", url, headers=headers, cookies=self.__cookie)
        return response.text