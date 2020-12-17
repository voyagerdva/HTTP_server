import Pages # вопрос - импортировать Pages, или унаследовать его?
import json

class UserQuerySpecification():
    # def __init__(self, body):
    #     self.paging = pages or None

    def __init__(self, body):
        paging = Pages(list(body.values())[0])

    def getPageStart(self):
        return self.paging.getCurrentPosition()

    def getPageSize(self):
        return self.paging.getPageSize()

    def deserialize(self):
        return self.__dict__()

    def __dict__(self):
        return '{"paging":%s}' % (self.paging)

# pages = Pages(body)