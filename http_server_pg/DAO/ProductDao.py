import json

class ProductDao:
    def __init__(self):
        pass

    def insert(self, lastPath, body):
        respBody = lastPath + "/respBody"
        return respBody

    def update(self, lastPath, body):
        respBody = lastPath + "/respBody"
        return respBody

    def select(self, lastPath):
        return str(lastPath), "/productSelect"

    def delete(self, lastPath, body):
        respBody = lastPath + "/respBody"
        return respBody
