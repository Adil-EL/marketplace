from flask import Blueprint, jsonify, redirect, request
from flask_cors import CORS

from app.db import get_laptops, get_laptops_filtred, get_laptops_sorted

laptops_api_v1 = Blueprint(
    'laptops_api_v1', 'laptops_api_v1',url_prefix= '/api/v1/laptops')

CORS(laptops_api_v1)

@laptops_api_v1.route('/',methods = ['GET'])
def api_get_laptops():
    laptops = get_laptops()
    response = {
        'laptops' : laptops,
        'total_results':10
    }

    return jsonify(response)

@laptops_api_v1.route('/filters',methods = ['GET', 'POST'])
def api_get_laptops_filters():

    filters = {}
    source = request.args.getlist('source')
    print("\n ************ \n")
    print(source)
    print("\n ************ \n")

    if source :
        filters['source'] = source


    print("\n ************ \n")
    print(filters)
    print("\n ************ \n")

    total_results,laptops = get_laptops_filtred(filters)
    response = {
        'total_results':total_results,
         'laptops' : laptops
    }

    return  jsonify(response)

@laptops_api_v1.route('/order')
def api_get_laptops_sorted():

    filters = {}
    #sort_variables = []
    # directions = []
    sort_variables = str(request.args.getlist('sort'))
    sort_variables=sort_variables[2:-2]
    sort_variables=sort_variables.split(',')
    print("\n ************ This is it \n")
    print(sort_variables)
    # print(directions)
    print("\n ************ \n")
    #sort_variables =['price','url']

    # try:
    #     sort_variables = request.args.getlist('sort')
    #     sort_variables=sort_variables[2:-2]
    #     sort_variables=sort_variables.split(',')


    # except:
    #     pass
    
    # try :
    #     directions = request.args.getlist('direction')
    # except: 
    #     pass
 
 




    total_results,laptops = get_laptops_sorted(filters,sort_variables)
    response = {
        'total_results':total_results,
         'laptops' : laptops
    }

    return  jsonify(response)