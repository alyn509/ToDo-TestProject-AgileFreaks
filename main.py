from flask import Flask, jsonify, request, abort
from todos import ToDoRepository, Status
from todos.status import ALL

app = Flask(__name__)
todos_repo = ToDoRepository()
todos_repo.add("make coffee", Status.INACTIVE.value)
todos_repo.add("toast_bread")


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
def create():
    to_do = request.get_json()
    if not to_do.get('name') or len(to_do.keys()) != 1:
        abort(400)
    else:
        todos_repo.add(to_do['name'])
        return list_all()
