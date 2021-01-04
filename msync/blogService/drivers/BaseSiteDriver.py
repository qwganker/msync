from abc import ABCMeta, abstractclassmethod

class BaseSiteDriver(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    '''
    新增
    '''
    @abstractclassmethod
    def add(cls, param):
        pass

    '''
    更新
    '''
    @abstractclassmethod
    def update(cls, param):
        pass

    '''
    获取博客分类
    '''
    @abstractclassmethod
    def fetchBlogCategory(cls, param=None):
        pass

    '''
    获取某一个分类下的文章列表
    '''
    @abstractclassmethod
    def fetchBlogList(cls, param=None):
        pass

    @abstractclassmethod
    def fetchBlogContent(cls, param=None):
        pass