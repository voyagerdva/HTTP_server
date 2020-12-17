import unittest
from fixtures import fixtures as fx
import requests
import json

class myTestHTTPServerGet(unittest.TestCase):
    def test_HTTPServerUserSelect(self):
        (myHOST, myPATH, myHeaders, userDtoDictTest) = fx.fixtureHTTPGetUserSelect(22)
        resp = requests.get(myHOST+myPATH, headers=myHeaders)
        respDict = json.loads(resp.text)
        respDictTest = (respDict['id'],
                        respDict['firstName'],
                        respDict['lastName'])
        print("this is 1 GET test User SELECT, done!!!")
        self.assertEqual(respDictTest, userDtoDictTest)

    def test_HTTPServerProductSelect(self):
        (myURL, myPath, myHeader, response) = fx.fixtureHTTPGetProductSelect(443322)
        resp = requests.get(myURL+myPath, headers=myHeader)
        respSplit = resp.text.split("?")
        print(" тест GET Product select")
        self.assertEqual(respSplit[0]+respSplit[1], response)
