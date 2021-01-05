from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import requests
import json

from .drivers.SiteDriverFactory import SiteDriverFactory
from common.HttpResult import HttpResult

class BlogPublishService(View):

    '''
    发布
    '''
    def post(self, request, format=None):

        reqParam = JSONParser().parse(request)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass

        siteDriver.add(reqParam["text"])

        return HttpResult.ok(info="发布成功")

class BlogCateService(View):

    '''
    获取分类
    '''
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass
        return siteDriver.fetchBlogCategory()

class BlogListService(View):

    '''
    获取分类下的文章列表
    '''
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        print(reqParam["id"])

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass
        result = siteDriver.fetchBlogList(reqParam["id"])

        return HttpResult.ok(info="获取成功", data=result)


class BlogContentService(View):
    '''
    获取内容
    '''
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        print(reqParam)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass

        result = siteDriver.fetchBlogContent(reqParam)

        return HttpResult.ok(info="获取成功", data=result)

    '''
    更新内容
    '''
    def put(self, request, format=None):
        reqParam = JSONParser().parse(request)
        print(reqParam)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass

        result = siteDriver.updateBlogContent(reqParam)

        return HttpResult.ok(info="更新成功", data=result)


class BlogPublishService(View):
    '''
    发布
    '''
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        print(reqParam)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass

        return siteDriver.publishBlog(reqParam)

    '''
    删除
    '''
    def delete(self, request, format=None):
        reqParam = JSONParser().parse(request)
        print(reqParam)

        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        if None == siteDriver:
            pass

        return siteDriver.deleteBlog(reqParam)
