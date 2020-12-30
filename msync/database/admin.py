from django.contrib import admin
from .models import Article, ArticleType, Site


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'createDateTime']


@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'item']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'address']
