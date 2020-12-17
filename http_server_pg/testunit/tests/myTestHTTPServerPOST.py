import unittest
from fixtures import fixtures as fx
import requests
import json


class myTestHTTPServerPOST(unittest.TestCase):

    def test_HTTPServerUserInsert(self):
        (myHOST, myPATH, myHeaders, userDtoDict, userDtoDictTest) = fx.fixtureHTTPPostUserInsert()
        resp = requests.post(myHOST+myPATH, headers=myHeaders, json=userDtoDict)
        respDict = json.loads(resp.text)
        respDictTest = (respDict['firstName'], respDict['lastName'])
        print("this is 1 POST test User INSERT, done!!!")
        self.assertEqual(respDictTest, userDtoDictTest)

    def test_HTTPServerPostMyControllerUserUpdate(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserUpdate(9)
        resp = requests.post(myURL + myPath, json=myBody, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест  POST User update")
        self.assertEqual(respSplit[0] + respSplit[1], response)

    def test_HTTPServerPostMyControllerUserDelete(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserDelete(9)
        resp = requests.post(myURL + myPath, json=myBody, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест  POST User delete")
        self.assertEqual(respSplit[0] + respSplit[1], response)

    def test_HTTPServerProductInsert(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostProductInsert(9)
        resp = requests.post(myURL + myPath, json=myBody, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест  POST Product insert")
        self.assertEqual(respSplit[0] + respSplit[1], response)

    def test_HTTPServerPostMyControllerProductUpdate(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostProductUpdate(9)
        resp = requests.post(myURL + myPath, json=myBody, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест pro up")
        self.assertEqual(respSplit[0] + respSplit[1], response)

    def test_HTTPServerPostMyControllerProductDelete(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostProductDelete(9)
        resp = requests.post(myURL + myPath, json=myBody, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест POST Product delete")
        self.assertEqual(respSplit[0] + respSplit[1], response)