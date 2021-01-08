from abc import ABCMeta, abstractclassmethod

class BaseSiteDriver(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    '''
    获取博客分类
    '''
    @abstractclassmethod
    def fetchBlogCateList(cls, param=None):
        pass

    '''
    获取某一个分类下的文章列表
    '''
    @abstractclassmethod
    def fetchBlogListInCate(cls, param=None):
        pass

    @abstractclassmethod
    def fetchBlog(cls, param=None):
        pass

    '''
    更新
    '''
    @abstractclassmethod
    def updateBlog(cls, param):
        pass

    '''
    发布
    '''
    @abstractclassmethod
    def publishBlog(cls, param):
        pass

    '''
    删除
    '''
    @abstractclassmethod
    def deleteBlog(cls, param):
        pass
