import datetime

class TimeUtils:
    @staticmethod
    def getNow():
        return datetime.datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def getNowDate():
        now = datetime.date.today()
        return now.strftime("%Y-%m-%d")

    @staticmethod
    def getNowDateTime2():
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    @staticmethod
    def getNowHour():
        return datetime.datetime.now().strftime("%H")

    @staticmethod
    def getNowDateTime():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def getTomorrowDate():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")

    @staticmethod
    def getNextDate(days):
        tomorrow = datetime.date.today() + datetime.timedelta(days=days)
        return tomorrow.strftime("%Y-%m-%d")

    @staticmethod
    def getPreviousDate(days):
        date = datetime.date.today() - datetime.timedelta(days=days)
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def getyesterdayDate():
        tomorrow = datetime.date.today() - datetime.timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")
    
    @staticmethod
    def formatStrDate(strDate):
        return datetime.datetime.strptime(strDate, '%Y-%m-%d').strftime('%Y-%m-%d')

