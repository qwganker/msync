from django.views.generic import View
from rest_framework.parsers import JSONParser

from .sitedrivers.SiteDriverFactory import SiteDriverFactory


class BlogListCategortyService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogCategoryList()

class BlogListService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchBlogList(reqParam)

class BlogFetchContentService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.fetchContentBlog(reqParam)

class BlogPublishUpdateService(View):
    def put(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.publishUpdateBlog(reqParam)

class BlogPublishNewService(View):
    def post(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.publishNewBlog(reqParam)

class BlogDeleteService(View):
    def delete(self, request):
        reqParam = JSONParser().parse(request)
        siteDriver = SiteDriverFactory.create(reqParam["siteType"])
        return siteDriver.deleteBlog(reqParam)
