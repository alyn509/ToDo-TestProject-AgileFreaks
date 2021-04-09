from flask import Flask, jsonify, g
from flask_expects_json import expects_json
from todos import ToDoRepository, Status
from marshmallow import ValidationError
from todos.status import ALL

app = Flask(__name__)
todos_repo = ToDoRepository()
todos_repo.add("make coffee", Status.INACTIVE.value)
todos_repo.add("toast_bread")

schema_create = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name']
}


@app.route('/v1/todos')
@app.route('/v1/todos/')
@app.route('/v1/todos/<status>')
def list_all(status=ALL) -> object:
    if status != ALL and status not in Status.value2member_map_:
        return jsonify("Status not found"), 400
    todos_list = todos_repo.list_all(status)
    return jsonify({
        'items': [
            x.to_dict() for x in todos_list
        ],
        'details': {
            'activeToDos': sum(map(lambda x: x.has_status(Status.ACTIVE.value), todos_repo.list_all()))
        }
    })


@app.route('/v1/todos', methods=['POST'])
@app.route('/v1/todos/', methods=['POST'])
@expects_json(schema_create)
def create():
    try:
        to_do = g.data
        todos_repo.add(to_do['name'])
        return list_all()
    except ValidationError as err:
        return jsonify(err.messages), 400


@app.route('/v1/todos/<identifier>', methods=['DELETE'])
def delete(identifier):
    try:
        index = todos_repo.get(int(identifier))
        if index is None:
            return jsonify("item with index %d does not exist" % int(identifier)), 404
        todos_repo.remove(index)
        return jsonify(identifier)
    except ValueError as err:
        return jsonify(str(err)), 400


@app.route('/v1/todos', methods=['DELETE'])
@app.route('/v1/todos/', methods=['DELETE'])
def clear():
    todos_repo.clear()
    return list_all()
