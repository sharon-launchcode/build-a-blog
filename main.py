from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog-user@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#according to the video, this is a persistent class configured to have its objexts stored in the database
class Task(db.Model):
#according to the video, this is all that is necessary to give each Task object a unique integer
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html',title="Get It Done!", tasks=tasks)
#shields the app from imports unless the main.py file is run ...hence the name if name is main
#to run a python shell in flask type python not python main.py just python puts you in python shell
#this allows you to test databases and put data into databases that is application orientefd
if __name__ == '__main__':
    app.run()