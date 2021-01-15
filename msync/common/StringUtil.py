
class StringUtil:

    @staticmethod
    def removeBlankAndBreakLine(string):
        return string.replace('\n', '').replace('\r', '')

    @staticmethod
    def objectStringLen(obj):
        return str(len(str(obj)))