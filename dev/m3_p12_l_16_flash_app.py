# import os
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    render_template,
    redirect,
    url_for
)

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = "secret_key"


# BEGIN (write your solution here)
@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'index.html',
        messages=messages,
    )


@app.route('/courses', methods=['POST'])
def courses_flash():
    flash('Course Added', 'success')
    # url_main = url_for('index')
    return redirect(url_for('index'))

# END


# @app.route('/users/')
# def users():
#     return 'Users Page'


# @app.route('/users/<id>')
# def users_page(id):
#     return f'User ID: {id}'


# @app.route('/')
# def index():
#     url1 = url_for('users')  # Генерация URL для маршрута 'users'
#     # Генерация URL для маршрута 'users_page' с параметром id=3
#     url2 = url_for('users_page', id=3)
#     return f'URL for Users: {url1}, URL for User 3: {url2}'
