from .csdn.CsdnDriver import CsdnDriver
from .jianshu.JianshuDriver import JianshuDriver
from .oschina.OschinaDriver import OschinaDriver
from .toutiao.ToutiaoDriver import ToutiaoDriver
from .juejin.JuejinDriver import JuejinDriver


class SiteDriverFactory():

    @staticmethod
    def create(siteType):
        if siteType == 'jianshu':
            return JianshuDriver()
        elif siteType == 'csdn':
            return CsdnDriver()
        elif siteType == 'toutiao':
            return ToutiaoDriver()
        elif siteType == 'oschina':
            return OschinaDriver()
        elif siteType == 'juejin':
            return JuejinDriver()
        else:
            return None
