class Pages():
    # def __init__(self, currentPosition, pageSize):
    def __init__(self, pageValue):
        # self.currentPosition = list(list(pageValue.values())[0].values())[0]
        # self.pageSize = list(list(pageValue.values())[0].values())[1]
        self.currentPosition = currentPosition
        self.pageSize = pageSize

    def getCurrentPosition(self):
        return self.currentPosition

    def getPageSize(self):
        return self.pageSize

    def deserialize(self):
        return self.__dict__()

    def __dict__(self):
        return '{"currentPosition":%s, "pageSize":%s}' % (self.currentPosition, self.pageSize)

    # ** list(body.values())[0]