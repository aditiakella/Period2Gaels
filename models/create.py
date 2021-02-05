from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///tweeterDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    nickname = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, key='email')
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)

def user_create(user_dict):
    """prepare data for primary table extracting from form"""
    user = Users(name=user_dict["name"], password=user_dict["password"], email=user_dict["email"], nickname=user_dict["nickname"])
    """add and commit data to user table"""
    db.session.add(user)
    db.session.commit()

def users_query_all():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.name, 'password': user.password, 'email': user.email, 'nickname': user.nickname}
        # filter email
    return records

if __name__ == "__main__":
    """create each table"""
    db.create_all()
    try:
        user_dict = {'name': 'Aditi Akella', 'password': 'aditi',
                     'email': 'aditi.s.akella@gmail.com', 'nickname': 'Aditi'}
        user_create(user_dict)
        u2 = Users(name='Sophie Bulkin', nickname='Sophie', email='tesla@example.com', password="sophie")
        u3 = Users(name='Grace Le', nickname='Grace', email='agbell@example.com', password="grace")
        u4 = Users(name='Luke Manning', nickname='Luke', email='eliw@example.com', password="luke")
        session.add_all([u2, u3, u4])
        session.commit()
    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print(row.nickname)
        print(row.email)
        print(row.password)

"""
Test on Terminal from IntelliJ
MacBook-Pro-2:flask-idea-homesiteZ johnmortensen$ cd models
MacBook-Pro-2:models johnmortensen$ sqlite3
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open createDB
sqlite> .tables
users
sqlite> select * from users;
1|Thomas Edison|Toby|tedison@example.com
2|Nicholas Tesla|Niko|ntesla@example.com
3|Alexander Graham Bell|Lex|agbell@example.com
4|Eli Whitney|Whit|eliw@example.com
"""