from pymongo import MongoClient, DESCENDING, ASCENDING
from app.db import get_laptops_sorted, get_laptops

LAPTOPS_DB_URI = "mongodb+srv://AdilLaptops:1234@laptops.m72a4.mongodb.net"
LAPTOPS_DB_NAME = "laptops"

db = MongoClient(LAPTOPS_DB_URI)[LAPTOPS_DB_NAME]
cursor  = db.tests.find({}).sort([("price", ASCENDING), ("source",DESCENDING)]).limit(20)[2]
print(cursor)




#num,cursor = get_laptops_sorted(db,filters,sort_variables)
#print(num)
