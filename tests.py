from pymongo import MongoClient, DESCENDING, ASCENDING
from app.db import get_laptops_sorted

LAPTOPS_DB_URI = "mongodb+srv://AdilLaptops:AdilLaptops@laptops.m72a4.mongodb.net"
LAPTOPS_DB_NAME = "laptops"

db = MongoClient(LAPTOPS_DB_URI)[LAPTOPS_DB_NAME]
cursor  = db.tests.find({}).sort([("price", ASCENDING), ("source",DESCENDING)]).limit(20)
#print(len(list(cursor)))
filters={}
sort_variables=['price','url']
num,cursor = get_laptops_sorted(db,filters,sort_variables)
print(num)
    