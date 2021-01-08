import msync.settings as CONF

from selenium import webdriver
import browser_cookie3

class PlatformDriver():

    @staticmethod
    def getDriver():
        return webdriver.Firefox(executable_path=CONF.PlatformDriverPath)

    @staticmethod
    def getCookies():
        if (CONF.PlatformDriverType == 'firefox'):
            return browser_cookie3.firefox()
        else:
            pass