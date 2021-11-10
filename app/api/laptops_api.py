from flask import Blueprint, request, jsonify
from app.db import get_laptops

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
