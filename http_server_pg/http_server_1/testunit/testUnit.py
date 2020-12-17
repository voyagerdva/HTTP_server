from myTestHTTPServerGet import myTestHTTPServerGet as GET
from myTestHTTPServerPOST import myTestHTTPServerPOST as POST

respPOST = POST()
respGET = GET()

respPOST.test_HTTPServerUserInsert()
respGET.test_HTTPServerUserSelect()
# respPOST.test_HTTPServerPostMyControllerUserUpdate()
# respPOST.test_HTTPServerPostMyControllerUserDelete()
# respPOST.test_HTTPServerProductInsert()
# respPOST.test_HTTPServerPostMyControllerProductUpdate()
# respPOST.test_HTTPServerPostMyControllerProductDelete()
# respGET.test_HTTPServerProductSelect()




