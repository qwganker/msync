from .jianshu.JianshuDriver import JianshuDriver
from .csdn.CsdnDriver import CsdnDriver
from .toutiao.ToutiaoDriver import ToutiaoDriver

class SiteDriverFactory():

    @staticmethod
    def create(siteType):
        if (siteType == 'jianshu'):
            return JianshuDriver()
        elif (siteType == 'csdn'):
            return CsdnDriver();
        elif (siteType == 'toutiao'):
            return ToutiaoDriver()
        else:
            return None
