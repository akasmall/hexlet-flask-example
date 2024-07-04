# from flask import request
from flask import Flask

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


# @app.route('/users', methods=['GET', 'POST'])
# def users():
#     if request.method == 'POST':
#         return 'Hello from POST /users'
#     return 'Hello from GET /users'


@app.get('/users')
def users_get():
    return 'GET /users'


# @app.post('/users')
# def users_post():
#     return 'POST /users'


@app.post('/users')
def users():
    return 'Users', 302
