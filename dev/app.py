import os
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from flask import session
from dev.repository import PostsRepository
from dev.validator import validate


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    # posts = {
    #     '79601c4e-d588-4d08-a68e-a2469c0d9fb3': {
    #         'title': 'заголовок',
    #         'body': 'тело',
    #         'id': '79601c4e-d588-4d08-a68e-a2469c0d9fb3'
    #     }
    # }   # это для теста, потом убрать

    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
    )


@app.route('/posts/new')
def new_post():
    post = {}
    errors = {}
    return render_template(
        'posts/new.html',
        post=post,
        errors=errors,
    )


@app.post('/posts')
def posts_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
        ), 422
    id_ = repo.save(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id_
    return resp


# BEGIN (write your solution here)
# Форма редактирования поста: GET /posts/<id>/update
# и
# Форма редактирования поста: POST /posts/<id>/update
@app.route('/posts/<item>/update', methods=['get', 'post'])
def post_edit(item):
    repo = PostsRepository()
    # post = repo.find(item)
    # post = {
    #     'title': 'заголовок',
    #     'body': 'тело',
    #     'id': '79601c4e-d588-4d08-a68e-a2469c0d9fb3'
    # }
    if request.method == 'GET':
        # Код для обработки GET запроса
        return 'Вы отправили GET запрос'
    elif request.method == 'POST':
        # Код для обработки POST запроса
        return 'Вы отправили POST запрос'


# Обновление поста: POST / posts / <id > /update
# @app.route('/posts/<id_>/update', methods=['post'])
# def post_update(id_):

#     return id_
# END
# В этой практике вам предстоит попрактиковаться в UPDATE операций CRUD.
# Для обновления ресурса сперва его нужно получить из хранилища и заполнить
# форму редактирования, а затем обновить, получив и провалидировав новые
# данные из формы.
# Также оповестите пользователя об успешной операции с помощью флеш - сообщений.
# src / app.py
# Реализуйте следующие обработчики:
# Форма редактирования поста: GET / posts / <id > /update
# Обновление поста: POST / posts / <id > /update
# Посты содержат два поля: title и body. Они обязательны к заполнению.
# Валидация уже написана, но не забудьте про вывод ошибок валидации.
# После каждого успешного действия нужно добавлять флеш - сообщение
# 'Post has been updated' и выводить его на списке постов.
# templates / posts / index.html
# Реализуйте вывод списка постов. В списке выводится title поста
# и ссылка Edit на страницу его редактирования.
# templates / posts / edit.html
# Форма для редактирования поста. Общая часть формы уже выделена
# в шаблон form.html, подключите его по аналогии с templates / posts / new.html.
# Подсказки
# Include
# Для редиректов в обработчиках используйте именованный роутинг
