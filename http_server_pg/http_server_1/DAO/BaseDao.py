from contextlib import closing
import postgresql

PROTOCOL = "pq"
USER_NAME = 'postgres'
PASSWORD = 'postgres'
HOST = 'localHOST'
PORT = 5432
BASE_NAME = "traindb"


class BaseDao:
    def __init__(self):
        pass


    def connectDB(self):
        return postgresql.open(PROTOCOL + "://" +
                               USER_NAME + ":"+
                               PASSWORD + "@" +
                               HOST + ":" + str(PORT) + '/' +
                               BASE_NAME)

