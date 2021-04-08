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
    todos_list = todos_repo.list_all(status)
    return jsonify({
        'items': [
            x.to_dict() for x in todos_list
        ],
        'details': {
            'activeToDos': sum(map(lambda x: x.has_status(Status.ACTIVE.value), todos_list))
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
