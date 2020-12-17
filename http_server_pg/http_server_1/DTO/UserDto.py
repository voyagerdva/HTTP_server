import time


class UserDto():
    def __init__(self, userEntity):
        if userEntity != None:
            self.id = userEntity.id
            self.firstName = userEntity.firstName
            self.lastName = userEntity.lastName
            self.timeRegistration = time.asctime()

    def deserialize(self, userEntityList):
        self.userDtoList = []
        for userEntity in userEntityList:
            self.id = userEntity.id
            self.firstName = userEntity.firstName
            self.lastName = userEntity.lastName
            self.timeRegistration = time.asctime()
            self.userDtoList.append('{"id":%s,'
                                    '"firstName":"%s",'
                                    '"lastName":"%s",'
                                    '"timeRegistration":"%s"}' % \
               (self.id, self.firstName, self.lastName, self.timeRegistration))

        while str(self.userDtoList).find("\'{") > 0:
            i = str(self.userDtoList).find("\'{")
            self.userDtoListStr = str(self.userDtoList)[:i] + "{" + str(self.userDtoList)[i + len("\'{"):]

        while self.userDtoList.find("}\'") > 0:
            i = self.userDtoList.find("}\'")
            self.userDtoList = self.userDtoList[:i] + "}" + self.userDtoList[i + len("}\'"):]

        return self.userDtoList

    # def deserialize(self):
    #     return self.__repr__()
    #
    # def __repr__(self):
    #     return '{"id":%s,"firstName":"%s","lastName":"%s","timeRegistration":"%s"}' % \
    #            (self.id, self.firstName, self.lastName, self.timeRegistration)
