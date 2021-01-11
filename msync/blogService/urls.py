from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^blog/list/category$", BlogListCateService.as_view()),
    url(r"^blog/list$", BlogListService.as_view()),
    url(r"^blog/fetch/content$", BlogFetchContetnService.as_view()),
    url(r"^blog/publish/update$", BlogPublishUpdateService.as_view()),
    url(r"^blog/publish/new$", BlogPublishNewService.as_view()),
    url(r"^blog/delete$", BlogDeleteService.as_view()),
]
