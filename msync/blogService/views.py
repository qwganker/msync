from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import requests
import json

from .sitedrivers.SiteDriverFactory import SiteDriverFactory
from common.HttpResult import HttpResult

class BlogCateListService(View):
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogCateList()

class BlogListInCateService(View):
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogListInCate(reqParam)

class BlogFetchService(View):
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlog(reqParam)

class BlogUpdateService(View):
    def put(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.updateBlog(reqParam)

class BlogPublishService(View):
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.publishBlog(reqParam)

class BlogDeleteService(View):
    def delete(self, request, format=None):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.deleteBlog(reqParam)

class BlogBatchPublishService(View):
    def post(self, request, format=None):
        reqParam = JSONParser().parse(request)

        for site in reqParam['sites']:
            siteDriver = SiteDriverFactory.create(site)
            siteDriver.publishBlog(reqParam)
        
        return HttpResult.ok(info="批量发布成功")
