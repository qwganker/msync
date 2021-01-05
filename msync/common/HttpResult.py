import json
from django.http import HttpResponse

class HttpResult():
    def __init__(self, *args, **kwargs):
        self.__data = {}
        self.__data["info"] = ""

    def setCode(self, code):
        self.__data["code"] = code

    def setInfo(self, info):
        self.__data["info"] = info

    def setData(self, data):
        self.__data["data"] = data

    def dumps(self):
        return json.dumps(self.__data)

    def output(self):
        return HttpResponse(json.dumps(self.__data, ensure_ascii=False), content_type="application/json,charset=utf-8");

    @staticmethod
    def new(code, info='', data=''):
        resp = HttpResult()
        resp.setCode(code)
        resp.setInfo(info)
        resp.setData(data)
        return resp.output()

    @staticmethod
    def ok(info='', data=''):
        resp = HttpResult()
        resp.setCode(200)
        resp.setInfo(info)
        resp.setData(data)
        return resp.output()

    @staticmethod
    def error(code=500, info='', data=''):
        resp = HttpResult()
        resp.setCode(code)
        resp.setInfo(info)
        resp.setData(data)
        return resp.output()

