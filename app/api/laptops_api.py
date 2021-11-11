from flask import Blueprint, request, jsonify
from app.db import get_laptops,get_laptops_filtred

from flask_cors import CORS

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

    if source :
        filters['source'] = source

    total_results,laptops = get_laptops_filtred(filters)
    response = {
        'total_results':total_results,
         'laptops' : laptops
    }

    return jsonify(response)