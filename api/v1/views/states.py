#!/usr/bin/python3
"""
View for handling default RESTFUL API actions
"""
from flask import jsonify, request, abort
from api.v1.views import app_views, storage
from models.state import State
