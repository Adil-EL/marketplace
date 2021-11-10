"""
This module manages all the interactions with MongoDB  via the API.
When profetionnals want to add a product or updateOne
Create a profetionnal account


"""



from flask import current_app, g 
from werkzeug.local import LocalProxy

from pymongo import MongoClient

def get_db():
    """
    Configuration method to return db instance
    """

    db = getattr(g, "_database", None)
    LAPTOPS_DB_URI = current_app.config["LAPTOPS_DB_URI"]
    LAPTOPS_DB_NAME = current_app.config["LAPTOPS_DB_NAME"]
    
    if db is None:
        db = g._database = MongoClient(LAPTOPS_DB_URI)[LAPTOPS_DB_NAME]
    
    return db 

# Use LocalProxy to read the global db instance with just `db`
db  = LocalProxy(get_db) 


def get_laptops():
    """
    Return a cursor list of laptops
    to be improved ...
    """
    cursor = db.laptops.find()
    print(cursor)
    laptops = cursor.limit(10)

    return list(laptops)

