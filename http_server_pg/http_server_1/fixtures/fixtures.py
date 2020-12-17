from testunit.Entities.User import User
from testunit.DTO.UserDto import UserDto
import json

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UserDto):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def fixtureHTTPPostUserInsert():
    myHOST = "http://localhost:9900"
    myPATH = "/users/insert"
    myHeaders = {"Content-type": "application/json", "Accept": "text/plain"}
    userEntity = User(25,
                      "Jhon",
                      "Smith",
                      4,
                      "USA, Whashington, st.Cooler, 75")
    userDto = UserDto(userEntity)
    userDtoStr = json.dumps(userDto, cls=PersonEncoder)
    userDtoDict = json.loads(userDtoStr)
    userDtoDictTest = (userDtoDict['firstName'], userDtoDict['lastName'])

    return (myHOST, myPATH, myHeaders, userDtoDict, userDtoDictTest)


def fixtureHTTPPostUserUpdate(id):
    myURL = "http://localhost:9900"
    myPath = "/users/update/" + str(id)
    myBody = {"id_city": 1111, "user_name": "Sara"}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/update" + "/" + str(id) + "/userUpdate"
    return (myURL, myPath, myBody, myHeader, response)


def fixtureHTTPPostUserDelete(id):
    myURL = "http://localhost:9900"
    myPath = "/users/delete/" + str(id)
    myBody = {"id_city": 1111, "user_name": "Sara"}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/delete" + "/" + str(id) + "/userDelete"
    return (myURL, myPath, myBody, myHeader, response)


def fixtureHTTPPostProductInsert(id):
    myURL = "http://localhost:9900"
    myPath = "/product/insert/" + str(id)
    myBody = {"id_product": 1111, "product_name": "Weel"}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/insert" + "/" + str(id) + "/productInsert"
    return (myURL, myPath, myBody, myHeader, response)


def fixtureHTTPPostProductUpdate(id):
    myURL = "http://localhost:9900"
    myPath = "/product/update/" + str(id)
    myBody = {"id_product": 1111, "product_name": "Weel"}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/update" + "/" + str(id) + "/productUpdate"
    return (myURL, myPath, myBody, myHeader, response)


def fixtureHTTPPostProductDelete(id):
    myURL = "http://localhost:9900"
    myPath = "/product/delete/" + str(id)
    myBody = {"id_product": 1111, "product_name": "Weel"}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/delete" + "/" + str(id) + "/productDelete"
    return (myURL, myPath, myBody, myHeader, response)


#################################################################

def fixtureHTTPGetUserSelect(id):
    userEntity = User(id,
                      "Jhon",
                      "Smith",
                      4,
                      "USA, Whashington, st.Cooler, 75")
    userDto = UserDto(userEntity)
    userDtoStr = json.dumps(userDto, cls=PersonEncoder)
    userDtoDict = json.loads(userDtoStr)
    userDtoDictTest = (userDtoDict['id'],
                       userDtoDict['firstName'],
                       userDtoDict['lastName'])
    myHOST = "http://localhost:9900"
    myPATH = "/users/select" + "/" + str(userDtoDict['id'])
    myHeaders = {"Content-type": "application/json", "Accept": "text/plain"}

    return (myHOST, myPATH, myHeaders, userDtoDictTest)


def fixtureHTTPGetProductSelect(id):
    myURL = "http://localhost:9900"
    myPath = "/product/select/" + str(id)
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    response = "/select" + "/" + str(id) + "/productSelect"
    return (myURL, myPath, myHeader, response)

#######################################################################################
