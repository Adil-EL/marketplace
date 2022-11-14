"""
This module manages all the interactions with MongoDB  via the API.
When profetionnals want to add a product or updateOne
Create a profetionnal account


"""



from flask import current_app, g 
from werkzeug.local import LocalProxy

from pymongo import MongoClient, DESCENDING, ASCENDING

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
    #print(cursor)
    laptops = cursor.limit(10)

    return list(laptops)

def build_query_sort_project(filters):
    """
    Builds the query predicate, 'sort', ansd 'projection' 
    attributes for a given filters dictionary. 
    """
    query = {}
    sort = [("price"), DESCENDING]
    project = {'title':1,'_id':0}

    if filters :
        if "source" in filters:
            query = {"source": {"$in": filters["source"]}}
            sort = [("price"), DESCENDING]
            project = {'title':1, 'price':1, 'url':1,'_id':0}
    
    return query, sort, project

def build_query_sort_project_2(filters,sort_variables):
    """
    Builds the query predicate, 'sort', ansd 'projection' 
    attributes for a given filters dictionary. 
    """
    query = {}
    sort = [] #[("price", ASCENDING), ("source",DESCENDING)])
    for variable in sort_variables:
        sort.append((variable,DESCENDING))
    project = {'title':1, 'price':1, 'url':1,'_id':0}

    if filters :
        if "source" in filters:
            query = {"source": {"$in": filters["source"]}}
            project = {'title':1, 'price':1, 'url':1,'_id':0}
    
    return query, sort, project

#-----------------------------------Filters ----------------------------------
def get_laptops_filtred(filters):

    """
    Returns a cursor to a list of laptops documents according to 
    the selected filters
    """

    query, sort, project = build_query_sort_project(filters)
    
    #query = {"source":{"$in" :["pc maroc"]}}
    


    if project :
        cursor  = db.laptops.find(query, project).sort("price",DESCENDING)
    
    else:
        cursor  = db.laptops.find() #.sort(sort)
    
    total_num_documents = 20 #db.laptops.count_documents(query) 

    return (total_num_documents, list(cursor))


#-------------------------------Sort --------------------------------------
def get_laptops_sorted(filters,sort_variables):

    """
    Returns a cursor to a list of laptops documents according to 
    the selected filters
    """

    query, sortt, project = build_query_sort_project_2(filters,sort_variables)
    

    if project :
        cursor  = db.laptops.find(query, project).sort(sortt)
    
    else:
        cursor  = db.laptops.find(query).sort(sortt)
    
    total_num_documents = cursor.count()
    #total_num_documents = 20

    return (total_num_documents, list(cursor))

