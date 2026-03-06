from todos import db, login_manager
from datetime import date
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(25), nullable=False, unique=True)
  email = db.Column(db.String(30), nullable=False, unique=True)
  firstname = db.Column(db.String(30), nullable=True)
  lastname = db.Column(db.String(30), nullable=True)
  password = db.Column(db.String(100), nullable=False)
  todos = db.relationship('Todo', backref='user')

  def __str__(self):
    return self.firstname
  
class Todo(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  created = db.Column(db.Date(), default=date.today())
  user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
  todolist = db.relationship('TodoList', backref='todo')

  def __str__(self):
    return self.created
  
class TodoList(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  task = db.Column(db.String(100), nullable=False)
  completed = db.Column(db.Boolean(), default=False)
  todo_id = db.Column(db.Integer(), db.ForeignKey('todo.id'))

  def __str__(self):
    return self.task