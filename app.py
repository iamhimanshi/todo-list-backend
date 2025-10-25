from flask import Flask, jsonify, request
import datetime 

app = Flask(__name__)

# in-memory to store todo
todo = [
    {
        "id": 1,
        "task": "Finish  assignments",
        "isCompleted": False,
        "createdAt": "2025-10-24T10:28:35"
    },
    {
        "id": 2,
        "task": "study for exams",
        "isCompleted": False,
        "createdAt": "2025-10-24T10:30:21"
    }
]

next_id = 3   # to assign id for new todo


@app.route('/')
def home():
    return jsonify({"message": "Todo API running"})


# get all todo
@app.route('/todo', methods=['GET'])
def get_all_todo():
    return jsonify(todo)


# add a new todo
@app.route('/todo', methods=['POST'])
def add_todo():
    global next_id
    data = request.get_json()

    if not data or 'task' not in data:
        return jsonify({"error": "task required"})

    new_todo = {
        "id": next_id,
        "task": data['task'],
        "isCompleted": False,
        "createdAt": datetime.datetime.now().isoformat()
    }
    todo.append(new_todo)
    next_id += 1
    print("added:", data['task'])
    return jsonify(new_todo)


# get a single todo by id 
@app.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    for t in todo:
        if t['id'] == todo_id:
            return jsonify(t)
    return jsonify({"error": "todo not found"})


# update a todo
@app.route('/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo_to_update = None

    for t in todo:
        if t['id'] == todo_id:
            todo_to_update = t
            break

    if not todo_to_update:
        return jsonify({"error": "todo not found"})

    if 'task' in data:
        todo_to_update['task'] = data['task']
    if 'isCompleted' in data:
        todo_to_update['isCompleted'] = data['isCompleted']

    print("updated:", todo_to_update)
    return jsonify(todo_to_update)


# delete a todo
@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo
    todo_to_delete = None

    for t in todo:
        if t['id'] == todo_id:
            todo_to_delete = t
            break

    if not todo_to_delete:
        return jsonify({"error": "todo not found"})

    todo.remove(todo_to_delete)
    print("deleted:", todo_to_delete['task'])
    return jsonify({"message": "todo deleted"})


if __name__ == '__main__':
    print("server running at port 5000")
    app.run(debug=True)
