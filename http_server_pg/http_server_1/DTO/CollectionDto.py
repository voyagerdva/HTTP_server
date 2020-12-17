import string
from DTO.UserDto import UserDto

class CollectionDto():
    def userDtoListDeserialize(self, userEntityList):
        self.userDtoList = []
        for userEntity in userEntityList:
            userDtoStr = UserDto(userEntity).deserialize()
            self.userDtoList.append(userDtoStr)
        return self.userDtoList


    def productDtoListDeserialize(self, userEntityList):
        pass

    def filtersListDeserialize(self):
        pass

    def collect(self, userEntityList):
        self.collection = '{"userList":%s}' % (self.userDtoListDeserialize(userEntityList), )

        while self.collection.find("\'{") > 0:
            i = self.collection.find("\'{")
            self.collection = self.collection[:i] + "{" + self.collection[i + len("\'{"):]

        while self.collection.find("}\'") > 0:
            i = self.collection.find("}\'")
            self.collection = self.collection[:i] + "}" + self.collection[i + len("}\'"):]

        return self.collection
### 2019-11-26