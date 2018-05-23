from flask import Flask, request, jsonify
from worker import integrate

app = Flask(__name__)
TASKS = {}

@app.route('/', methods=['GET'])
def list_tasks():
    task_id = request.args.get('id')
    if task_id and task_id.isdigit():
        task = TASKS[int(task_id)]
        return jsonify(task.get())

    tasks = {task_id: {'ready': task.ready()}
            for task_id, task in TASKS.items()}
    return jsonify(tasks)

@app.route('/', methods=['PUT'])
def put_task():
    f = request.json['f']
    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    d = request.json['d']
    size = request.json.get('size', 100)

    task_id = len(TASKS)
    TASKS[task_id] = integrate.delay(f, a, b, c, d, size)
    return jsonify({'task_id': task_id})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

