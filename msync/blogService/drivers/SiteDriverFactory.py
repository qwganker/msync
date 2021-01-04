from .jianshu.JianshuDriver import JianshuDriver
from .csdn.CsdnDriver import CsdnDriver


class SiteDriverFactory():

    @staticmethod
    def create(siteType):
        if (siteType == 'jianshu'):
            return JianshuDriver()
        elif (siteType == 'csdn'):
            return CsdnDriver();
        else:
            return None
