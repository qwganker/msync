from selenium import webdriver
import msync.settings as SYS_CONF


class WebDriver():

    def __init__(self):
        self.__driver = webdriver.Firefox(executable_path=SYS_CONF.PlatformDriverPath)

    def getDriver(self):
        return self.__driver

