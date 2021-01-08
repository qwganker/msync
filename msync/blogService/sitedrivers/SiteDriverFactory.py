from .jianshu.JianshuDriver import JianshuDriver
from .csdn.CsdnDriver import CsdnDriver
from .toutiao.ToutiaoDriver import ToutiaoDriver
from .oschina.OschinaDriver import OschinaDriver

class SiteDriverFactory():

    @staticmethod
    def create(siteType):
        if (siteType == 'jianshu'):
            return JianshuDriver()
        elif (siteType == 'csdn'):
            return CsdnDriver();
        elif (siteType == 'toutiao'):
            return ToutiaoDriver()
        elif (siteType == 'oschina'):
            return OschinaDriver()
        else:
            return None
