from flask import Flask, jsonify
from todos import ToDoList
app = Flask(__name__)
tds = ToDoList()


@app.route('/v1/todos')
@app.route('/v1/todos/')
@app.route('/v1/todos/<status>')
def list_all(status="all"):
    tds.append("make coffee")
    tds.append("toast_bread")
    return jsonify(tds.list_all(status))
