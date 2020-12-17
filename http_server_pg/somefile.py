# -*- coding: utf-8 -*-
from PIL import Image
import io
from sys import argv
from DAO.UserDao import UserDao
from DAO.ProductDao import ProductDao
from Entities.User import User
import json
from DTO.UserDto import UserDto
from QuerySpecification.Pages import Pages
from QuerySpecification.UserQuerySpecification import UserQuerySpecification
from DTO.CollectionDto import CollectionDto


class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class MyController(UserDao, ProductDao, User):
    def __init__(self):
        UserDao.__init__(self)
        ProductDao.__init__(self)

    def postRedirect(self, path, body):
        pathSplit = path.split('/')

        body = json.loads(body)

        if pathSplit[1] == '':
            return '/Your request was empty !!! $-) '

        elif pathSplit[1] == 'favicon.ico':
            return 'favicon_ico'

        elif pathSplit[1] == 'users' and pathSplit[2] == 'insert':
            userEntity = User(body['id'],
                              body['firstName'],
                              body['lastName'],
                              body['age'],
                              body['address'])
            newUserEntity = UserDao.insert(self, userEntity)
            userDto = UserDto(newUserEntity)
            userDTOstr = json.dumps(userDto, cls=ObjectEncoder)
            return userDTOstr

        elif pathSplit[1] == 'users' and pathSplit[2] == 'update':
            return UserDao.update(self, None, body)

        elif pathSplit[1] == 'users' and pathSplit[2] == 'delete':
            return UserDao.delete(self, None, body)

        elif pathSplit[1] == 'users' and pathSplit[2] == 'getList':
            userQuerySpecification = UserQuerySpecification(body)
            userEntityList = UserDao.getList(self, userQuerySpecification)
            userDtoList = UserDto(None).deserialize(userEntityList)
            # collectionDto = CollectionDto().collect(userEntityList)
            return userDtoList

        elif pathSplit[1] == 'product' and pathSplit[2] == 'insert':
            return ProductDao.insert(self, None, body)

        elif pathSplit[1] == 'product' and pathSplit[2] == 'update':
            return ProductDao.update(self, None, body)

        elif pathSplit[1] == 'product' and pathSplit[2] == 'delete':
            return ProductDao.delete(self, None, body)

        else:
            return 404

    def getRedirect(self, path):
        pathSplit = path.split('/')

        if pathSplit[1] == '':
            return '/Your request was empty !!! $-) '

        elif pathSplit[1] == 'favicon.ico':
            return 'favicon_ico'

        elif len(pathSplit) == 4 and pathSplit[1] == 'users' and pathSplit[2] == 'select':
            userEntityById = UserDao.getById(self, int(pathSplit[3]))
            userDto = UserDto(userEntityById)
            userDTOstr = json.dumps(userDto, cls=ObjectEncoder)
            return userDTOstr

        elif len(pathSplit) == 4 and pathSplit[1] == 'product' and pathSplit[2] == 'select':
            return ProductDao.select(self, int(pathSplit[3]))

        else:
            return 404

