#!/usr/bin/python3
"""
    Retrieves JSON responses
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON status response """
    response = jsonify({"status": "OK"})
    response.headers['Content-Type'] = 'application/json'
    return response


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Retrieves the number of each object type """
    count_obj = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    for obj in count_obj.keys():
        count_obj[obj] = storage.count(count_obj.get(obj))
    response = jsonify(count_obj)
    response.headers['Content-Type'] = 'application/json'
    return response
