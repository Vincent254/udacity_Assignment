import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps
from bson import json_util

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    print(dumps(request))
    if request:
        try:

            uri = os.environ['DBConnectionMongo']
            client = pymongo.MongoClient(uri)
            database = client['machocosmosdb']
            collection = database['advertisements']

            result = collection.insert_one(request)
            print("Inserted advert " , result.inserted_id)
            return func.HttpResponse(req.get_body())

        except ValueError as e:
            print("============ Value Error ====================")
            print(e.__dict__);
            #print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )



