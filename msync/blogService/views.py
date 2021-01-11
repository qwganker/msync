from django.views.generic import View
from rest_framework.parsers import JSONParser

from .sitedrivers.SiteDriverFactory import SiteDriverFactory


class BlogListCateService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogCateList()

class BlogListService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogListInCate(reqParam)

class BlogFetchContetnService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlog(reqParam)

class BlogPublishUpdateService(View):
    def put(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.updateBlog(reqParam)

class BlogPublishNewService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.publishBlog(reqParam)

class BlogDeleteService(View):
    def delete(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.deleteBlog(reqParam)
