from blogService.sitedrivers.BaseSiteDriver import BaseSiteDriver

from common.platformdriver import PlatformDriver

class OschinaDriver(BaseSiteDriver):
    def __init__(self, *args, **kwargs):
        self.__cookie = PlatformDriver.getCookies()

    def __setDriverCookie(self, driver):
        for c in self.__cookie:
            if 'oschina.net' in c.domain:
                isScure = True
                if (c.secure == 0):
                    isScure = False
                driver.add_cookie({'name' : c.name, 'value' : c.value, 'path' : c.path, 'secure': isScure})

    '''
    获取博客分类
    '''
    def fetchBlogCateList(self, param=None):
        pass

    '''
    获取某一个分类下的文章列表
    '''
    def fetchBlogListInCate(self, param=None):
        pass

    def fetchBlog(self, param=None):
        pass

    '''
    更新
    '''
    def updateBlog(self, param):
        pass

    '''
    发布
    '''
    def publishBlog(self, param):
        pass

    '''
    删除
    '''
    def deleteBlog(self, param):
        pass
