from DAO.BaseDao import BaseDao
import postgresql
from Entities.User import User
import json


class UserDao(BaseDao):
    def __init__(self):
        BaseDao.__init__(self)

    def getById(self, id):
        userFromDB = BaseDao.connectDB(self).query("SELECT * "
                                                   "FROM public.users "
                                                   "WHERE id = %s" % id)
        userEntity = User(userFromDB[0][0],
                          userFromDB[0][1],
                          userFromDB[0][2],
                          userFromDB[0][3],
                          userFromDB[0][4])
        return userEntity

    def getList(self, qSpec):
        listUserFromDB = self.connectDB().query("SELECT * "
                                                "FROM public.users "
                                                "LIMIT %s OFFSET %s" %
                                                (qSpec.getPageSize(),
                                                 qSpec.getPageStart()))
        listUserEntity = []
        for user in listUserFromDB:
            userEntity = User(user[0], user[1], user[2], user[3], user[4])
            listUserEntity.append(userEntity)

        return listUserEntity

    def insert(self, userEntity):
        firstNameUser = userEntity.firstName
        lastNameUser = userEntity.lastName
        ageUser = userEntity.age
        addressUser = userEntity.address

        ins = self.connectDB().prepare("INSERT INTO users (firstName, lastName, age, address) "
                                       "VALUES ($1, $2, $3, $4) "
                                       "RETURNING id")
        idUser = ins(firstNameUser, lastNameUser, ageUser, addressUser)[0][0]
        userEntity.id = idUser
        return userEntity

    def update(self, lastPath, body):
        respBody = lastPath + "/respBody"
        return respBody

    def delete(self, lastPath, body):
        respBody = lastPath + "/respBody"
        return respBody
