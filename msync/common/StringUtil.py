
class StringUtil:

    @staticmethod
    def removeBlankAndBreakLine(string):
        return string.replace('\n', '').replace('\r', '')