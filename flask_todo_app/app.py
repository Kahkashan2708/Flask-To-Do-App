from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple list to store tasks (temporary memory)
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
