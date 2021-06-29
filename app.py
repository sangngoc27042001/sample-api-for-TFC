from database import Database
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Hello"
@app.route("/add_user/<name>/<role>/<course>")
def add_user(name, role, course):
    Database.add_user(name, role, course)
    return Database.get_managae_data()
@app.route("/delete_user/<id>")
def delete_user(id):
    Database.delete_user(id)
    return Database.get_managae_data()

@app.route("/add_course/<name>")
def add_course(name):
    Database.add_course(name)
    return Database.get_managae_data()
@app.route("/delete_course/<id>")
def delete_course(id):
    Database.delete_course(id)
    return Database.get_managae_data()

@app.route("/get_manage_data")
def get_manage_data():
    return Database.get_managae_data()

if __name__=="__main__":
    app.run(debug=True)