from uuid import uuid4
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
        tasks.append({'id': str(uuid4()), 'title': title})
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
