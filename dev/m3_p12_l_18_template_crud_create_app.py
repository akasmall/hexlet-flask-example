import os
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
from dev.m3_p12_l_18_template_crud_create_repository import PostsRepository
from dev.m3_p12_l_18_template_crud_create_validator import validate


app = Flask(__name__)
# Загрузка переменных окружения из .env файла
app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
    )


# BEGIN (write your solution here)

@app.route('/posts/new')
def posts_new():
    title = ''
    body = ''
    return render_template('posts/new.html', title=title, body=body)


@app.route('/posts', methods=["GET", "POST"])
def posts_post():
    title = request.form.get('title')
    body = request.form.get('body')
    post = {"title": title, "body": body, }
    errors = validate(post)
    if errors:
        return render_template(
            'posts/new.html',
            title=title,
            body=body,
            errors=errors
        ), 422

    repo = PostsRepository()
    repo.save(post)

    flash('Post has been created', 'success')
    return redirect(url_for('posts_get'))

# END
#
#
# В этой практике вам предстоит попрактиковаться в CREATE операций CRUD.
# Чтобы добавить данные используется форма создания ресурса.
# Также введенные данные обязательно нужно провалидировать,
# чтобы в хранилище не попала некорректная информация.
# src / app.py
# Реализуйте следующие обработчики:
# Форма создания нового поста: GET / posts / new
# Создание поста: POST / posts
# Посты содержат два поля: title и body. Они обязательны к заполнению.
# Валидация уже написана, но не забудьте про вывод ошибок валидации.
# После каждого успешного действия нужно добавлять флеш -
# сообщение 'Post has been created' и выводить его на списке постов.
# templates / posts / new.html
# Форма для создания поста
# Подсказки
# Чтобы работать с репозиторием в обработчике,
# его нужно инициализировать по примеру в posts_get()
# Чтобы сохранить пост, используйте метод репозитория save()
# Для обработки незаполненных полей можно воспользоваться
# встроенным в шаблонизатор фильтром default()

# решение ментора
# # BEGIN
# @app.route('/posts/new')
# def new_post():
#     post = {}
#     errors = {}
#     return render_template(
#         'posts/new.html',
#         post=post,
#         errors=errors,
#     )


# @app.post('/posts')
# def posts_post():
#     repo = PostsRepository()
#     data = request.form.to_dict()
#     errors = validate(data)
#     if errors:
#         return render_template(
#             'posts/new.html',
#             post=data,
#             errors=errors,
#         ), 422
#     repo.save(data)
#     flash('Post has been created', 'success')
#     return redirect(url_for('posts_get'))
# # END
