from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^blog/publish$", BlogPublishService.as_view()),
    url(r"^blog/cate$", BlogCateService.as_view()),
    url(r"^blog/list$", BlogListInCateService.as_view()),
    url(r"^blog/content$", BlogContentService.as_view()),

]
