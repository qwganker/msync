from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^blog/publish$", BlogPublishService.as_view()),
    url(r"^blog/batch_publish$", BlogBatchPublishService.as_view()),
    url(r"^blog/cate_list$", BlogCateListService.as_view()),
    url(r"^blog/list_in_cate$", BlogListInCateService.as_view()),
    url(r"^blog/fetch$", BlogFetchService.as_view()),
    url(r"^blog/update$", BlogUpdateService.as_view()),
    url(r"^blog/delete$", BlogDeleteService.as_view()),
]
