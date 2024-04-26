#!/usr/bin/python3
""""
View for state objects that handle RESTful API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def state_get_all():
    """Method to retreive all state objects"""
    obj_list = []
    obj_state = storage.all("State")
    for i in obj_state.values():
        obj_list.append(i.to_json())

    return jsonify(obj_list)


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def state_create():
    """Method to create state route"""
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')
    if "name" not in state_json:
        abort(400, 'Missing name')

    new_state = State(**state_json)
    new_state.save()
    response = jsonify(new_state.to_json())
    response.status_code = 201

    return response


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def state_by_id(state_id):
    """Retrieves a state by ID"""
    get_state = storage.get("State", str(state_id))
    if get_state is None:
        abort(404)

    return jsonify(get_state.to_json())


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def state_put(state_id):
    """method to updates state object by id"""
    obj_state = request.get_json(silent=True)
    if obj_state is None:
        abort(400, 'Not a JSON')
    get_obj = storage.get("State", str(state_id))
    if get_obj is None:
        abort(404)
    for i, j in obj_state.items():
        if i not in ["id", "created_at", "updated_at"]:
            setattr(get_obj, i, j)
    get_obj.save()
    response = jsonify(get_obj.to_json())
    return response


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def state_delete_by_id(state_id):
    """method to delete a state  by id"""
    get_obj = storage.get("State", str(state_id))
    if get_obj is None:
        abort(404)

    storage.delete(get_obj)
    storage.save()

    return jsonify({})
