from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        tasks.append({'id': str(uuid4()), 'title': title})
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<task_id>/edit', methods=['GET'])
def edit_task_form(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    return render_template('edit_task.html', task=task)

@app.route('/tasks/<task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form.get('title')
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = title
            break
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks.xml')
def mobile_tasks():
    return '''
    <screen title="Tasks">
      <view style="padding: 20">
        <text style="font-size: 24">Tasks</text>
        <view>
          %s
        </view>
      </view>
    </screen>
    ''' % ''.join(f'<text>{t["title"]}</text>' for t in tasks), 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(debug=True)
