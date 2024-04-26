#!/usr/bin/python3
"""flask route that returns json status"""
from api.v1.views import app_views
from flask import jsonify, request
from models import app_views, storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route
    """
    response = {"status": "OK"}
    resp = jsonify(response)
    return resp


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    stats of object routes
    """
    obj = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    response = jsonify(obj)
    return response
