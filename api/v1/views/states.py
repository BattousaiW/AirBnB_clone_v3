#!/usr/bin/python3
"""flask route that returns json status"""
from api.v1.views import app_views
from flask import jsonify, request
from models import app_views, storage
