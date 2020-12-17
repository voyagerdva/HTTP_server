class ProductDto:
    def __init__(self, idProduct, name, quantity):
        self.id = idProduct
        self.name = name
        self.quantity = quantity

    def insert(self, lastPath, body):
        respBody = lastPath + '/respBody'
        return respBody

    def update(self, lastPath, body):
        respBody = lastPath + '/respBody'
        return respBody

    def select(self, lastPath):
        return str(lastPath), '/productSelect'

    def delete(self, lastPath, body):
        respBody = lastPath + '/respBody'
        return respBody
