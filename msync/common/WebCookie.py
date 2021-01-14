import browser_cookie3
import msync.settings as SYS_CONF

class WebCookie():

    def __init__(self):
        if SYS_CONF.PlatformDriverType == 'firefox':
            self.__allCookies = browser_cookie3.firefox()
        else:
            pass

    def getAllCookies(self):
        return self.__allCookies
