from abc import ABCMeta

class BaseSiteDriver(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    '''
    获取博客分类
    '''
    @classmethod
    def fetchBlogCategoryList(cls, param=None):
        pass

    '''
    获取博客列表
    '''
    @classmethod
    def fetchBlogList(cls, param=None):
        pass

    @classmethod
    def fetchContentBlog(cls, param=None):
        pass

    '''
    更新博客
    '''
    @classmethod
    def publishUpdateBlog(cls, param):
        pass

    '''
    发布新博客
    '''
    @classmethod
    def publishNewBlog(cls, param):
        pass

    '''
    删除
    '''
    @classmethod
    def deleteBlog(cls, param):
        pass
