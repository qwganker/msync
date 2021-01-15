from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver


class OschinaDriver(BaseSiteDriver):
    def __init__(self):
        super().__init__()

    '''
    获取博客分类
    '''
    def fetchBlogCategoryList(self, param=None):
        pass

    '''
    获取某一个分类下的文章列表
    '''
    def fetchBlogList(self, param=None):
        pass

    def fetchContentBlog(self, param=None):
        pass

    '''
    更新
    '''
    def publishUpdateBlog(self, param):
        pass

    '''
    发布
    '''
    def publishNewBlog(self, param):
        pass

    '''
    删除
    '''
    def deleteBlog(self, param):
        pass
