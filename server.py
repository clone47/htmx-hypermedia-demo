from flask import Flask, render_template, request

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
        tasks.append(title)
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
