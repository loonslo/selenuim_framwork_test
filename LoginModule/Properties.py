"""
@data:2020/6/10 13:34
@param:

"""


class Properties(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getDict(self, strName, dictName, value):
        if strName.find('.') > 0:
            k = strName.split('.')[0]
            dictName.setdefault(k, {})
            return self.__getDict(strName[len(k) + 1:], dictName[k], value)
        else:
            dictName[strName] = value
