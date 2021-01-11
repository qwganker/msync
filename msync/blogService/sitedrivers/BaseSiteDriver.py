from abc import ABCMeta

class BaseSiteDriver(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    '''
    获取博客分类
    '''
    @classmethod
    def fetchBlogCateList(cls, param=None):
        pass

    '''
    获取某一个分类下的文章列表
    '''
    @classmethod
    def fetchBlogListInCate(cls, param=None):
        pass

    @classmethod
    def fetchBlog(cls, param=None):
        pass

    '''
    更新
    '''
    @classmethod
    def updateBlog(cls, param):
        pass

    '''
    发布
    '''
    @classmethod
    def publishBlog(cls, param):
        pass

    '''
    删除
    '''
    @classmethod
    def deleteBlog(cls, param):
        pass
