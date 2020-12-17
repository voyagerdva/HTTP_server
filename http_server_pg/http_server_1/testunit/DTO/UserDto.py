class UserDto:
    def __init__(self, user):
        self.id = user.id
        self.firstName = user.firstName
        self.lastName = user.lastName
        self.age = user.age
        self.address = user.address