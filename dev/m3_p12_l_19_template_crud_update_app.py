import os
import uuid
import json
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
# from flask import session
from dev.m3_p12_l_19_template_crud_update_repository import PostsRepository
from dev.m3_p12_l_19_template_crud_update_validator import validate

# Путь к файлу, где будут храниться посты
POSTS_FILE = 'dev/posts.json'


def load_posts():
    try:
        with open(POSTS_FILE, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_posts(post):
    posts = load_posts()
    if not (post.get('title') and post.get('body')):
        raise Exception(f'Wrong data: {json.loads(post)}')
    if not post.get('id'):
        post['id'] = str(uuid.uuid4())
    posts[post['id']] = post
    with open(POSTS_FILE, 'w', encoding="utf-8") as f:
        json.dump(posts, f)
    return post['id']


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    posts = repo.content()
    # posts = load_posts()

    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages)
    # posts = {
    #     '79601c4e-d588-4d08-a68e-a2469c0d9fb3': {
    #         'title': 'заголовок 1',
    #         'body': 'тело 1',
    #         'id': '79601c4e-d588-4d08-a68e-a2469c0d9fb3'
    #     },
    #     '77777c4e-d588-4d08-a68e-a2469c0d9777': {
    #         'title': 'заголовок 2',
    #         'body': 'тело 2',
    #         'id': '77777c4e-d588-4d08-a68e-a2469c0d9777'
    #     }
    # }   # это для теста, потом убрать

    # return render_template(
    #     'posts/index.html',
    #     posts=posts,
    #     messages=messages,
    # )


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
    # id_ = save_posts(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id_
    return resp


# BEGIN (write your solution here)
# Форма редактирования поста: GET /posts/<id>/update
@app.route('/posts/<id_>/update', methods=['get'])
def post_edit(id_):
    repo = PostsRepository()
    post = repo.find(id_)
    # posts = load_posts()
    # if not posts.get(id_):
    #     pass
    # post = posts.get(id_)

    # post = {
    #     'title': 'заголовок',
    #     'body': 'тело',
    #     'id': '79601c4e-d588-4d08-a68e-a2469c0d9fb3'
    # }
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'posts/edit.html',
        post=post,
        id_=id_,
        messages=messages,
    )


# Обновление поста: POST / posts / <id > /update
@app.route('/posts/<id_>/update', methods=['post'])
def post_update(id_):
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
        ), 422
    # Загружаем существующие посты
    # posts = load_posts()
    # ищем пост
    # if not posts.get(id_):
    #     pass
    # post = posts.get(id_)
    # posts[str(len(posts) + 1)] = data
    # Сохраняем посты в файл
    # id_ = save_posts(posts)

    repo = PostsRepository()
    post = repo.find(id_)
    post.update(data)
    id_ = repo.save(post)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id_
    return resp

    # return redirect(url_for('posts'))
    # return 'Вы отправили POST запрос'

#
#
# END
# *В этой практике вам предстоит попрактиковаться в UPDATE операций CRUD.
# *Для обновления ресурса сперва его нужно получить из хранилища и заполнить
# *форму редактирования, а затем обновить, получив и провалидировав новые
# *данные из формы.
# *Также оповестите пользователя об успешной операции
# *с помощью флеш - сообщений.
# !src / app.py
# *Реализуйте следующие обработчики:
# *Форма редактирования поста: GET / posts / <id > /update
# *Обновление поста: POST / posts / <id > /update
# *Посты содержат два поля: title и body. Они обязательны к заполнению.
# *Валидация уже написана, но не забудьте про вывод ошибок валидации.
# *После каждого успешного действия нужно добавлять флеш - сообщение
# *'Post has been updated' и выводить его на списке постов.
# *templates / posts / index.html
# *Реализуйте вывод списка постов. В списке выводится title поста
# *и ссылка Edit на страницу его редактирования.
# *templates / posts / edit.html
# *Форма для редактирования поста. Общая часть формы уже выделена
# *в шаблон form.html, подключите его по аналогии
# *с templates / posts / new.html.
# !Подсказки
# TODO Include
# TODOДля редиректов в обработчиках используйте именованный роутинг


# !решение ментора
# ?# BEGIN
# *@app.route('/posts/<id>/update', methods=['GET', 'POST'])
# *def post_update(id):
# *    repo = PostsRepository()
# *    post = repo.find(id)

# *    if request.method == 'GET':
# *        return render_template(
# *            'posts/edit.html',
# *           post=post,
# *           errors={},
# *       )

# *   if request.method == 'POST':
# *       data = request.form.to_dict()
# *       data['id'] = id

# *       errors = validate(data)
# *       if errors:
# *           return render_template(
# *               'posts/edit.html',
# *               post=data,
# *               errors=errors,
# *           ), 422

# *       post['title'] = data.get('title', '')
# *       post['body'] = data.get('body', '')
# *       repo.save(post)
# *       flash('Post has been updated', 'success')
# *       return redirect(url_for('posts_get'))
# ?# END
