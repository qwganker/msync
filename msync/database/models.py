from django.db import models


class Article(models.Model):
    title = models.CharField('标题', blank=True, null=True, max_length=64)

    createDateTime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Site(models.Model):
    name = models.CharField('站点名字', null=True, blank=True, max_length=255)
    address = models.CharField('站点地址', null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = '站点'
        verbose_name_plural = '站点'


class ArticleType(models.Model):
    item = models.CharField('类型', blank=True, null=True, max_length=64)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'
