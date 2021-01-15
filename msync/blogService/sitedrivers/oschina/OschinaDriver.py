from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver


class OschinaDriver(BaseSiteDriver):
    def __init__(self):
        super().__init__()

    def fetchBlogCategoryList(self, param=None):
        """
        获取博客分类
        """
        pass

    def fetchBlogList(self, param=None):
        """
        获取某一个分类下的文章列表
        """
        pass

    def fetchContentBlog(self, param=None):
        pass

    def publishUpdateBlog(self, param):
        """
        更新
        """
        pass

    def publishNewBlog(self, param):
        """
        发布
        """
        pass

    def deleteBlog(self, param):
        """
        删除
        """
        pass
