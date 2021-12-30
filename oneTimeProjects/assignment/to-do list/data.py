from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    tasks = relationship("Tasklist", back_populates="user")


class Tasklist(db.Model):
    __tablename__ = "tasklist"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(250), unique=True, nullable=False)
    creation_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    user = relationship("Users", back_populates="tasks")
    item = relationship("Items", back_populates="task")


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(250))
    creation_date = db.Column(db.String(250), nullable=False)
    end_date = db.Column(db.String(250), nullable=False)
    task = relationship("Tasklist", back_populates="item")
    task_id = db.Column(db.Integer, db.ForeignKey("tasklist.id"))

# db.create_all()
# u = Users(
#     name="Suraj",
#     email="sg704992@gmail.com",
#     password="Hello123"
# )
# u.tasks=[
#         Tasklist(
#             name="Fuckers",
#             creation_date="Motherfuckers",
#             end_date="35 February, 2069"
#         )
#     ]
# db.session.add(u)
# db.session.commit()
# u = Users.query.all()
# print(u[0].name)