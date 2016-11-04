from pymongo import (
    MongoClient,
    errors
)


class Mongodb(object):
    """
    Handle mongodb connection
    """
 
    def __init__(self, uri, database):
        """
        Establish connection to mongoDB database

        :param uri: mongoDB URI
        :param database: database name
        """
        try:
            self.mongo_client = MongoClient(uri)
            self.mongodb = self.mongo_client[database]
            print "Connected successfully to: {}".format(database)
        except errors.ConnectionFailure, e:
            print "Could not connect to database: {}".format(e)

    def get_db(self):
        return self.mongodb
    
    def get_client(self):
        return self.mongo_client
