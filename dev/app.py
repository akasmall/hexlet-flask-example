import os
from dotenv import load_dotenv
from faker import Faker
from flask import Flask, render_template, request

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

fake = Faker()
Faker.seed(1234)


def generate(size):
    posts = []
    for _ in range(size):
        posts.append({
            'id': fake.uuid4(),
            'title': fake.sentence(),
            'body': fake.text(),
            'slug': fake.slug(),
        })
    return posts


class PostsRepository:
    def __init__(self, size):
        self.posts = generate(size)

    def content(self):
        return self.posts

    def find(self, slug):
        return next((post for post in self.posts if slug == post['slug']), None)


repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
def get_items(page, per_page):
    posts_page = repo.content()
    start = (page - 1) * per_page
    end = start + per_page
    return posts_page[start:end]

# @app.route('/posts', methods=['GET', 'POST'])
# @app.route('/posts', methods=['GET', 'POST'])


@app.route('/posts')
def post_():

    page = int(request.args.get('page', default=1, type=int))
    per_page = 5
    if not page:
        page = 1
    items = get_items(page, per_page)
    if not items:
        page -= 1
        items = get_items(page, per_page)
    return render_template('/posts/index.html', items=items, page=page)


@app.route('/posts/<slug>', methods=['GET', 'POST'])
# @app.route('/posts/<slug>')
def post_slug(slug):
    # posts_msg = repo.content()

    # page = request.args.get('page', default=1, type=int)
    # per = request.args.get('per', default=5, type=int)

    # start_idx = (page - 1) * per
    # end_idx = start_idx + per

    # posts_msg_on_page = posts_msg[start_idx:end_idx]
    # return render_template(
    #     '/posts/index.html',
    #     posts_msg=posts_msg_on_page)
    return render_template('/index.html')

    # page = int(request.args.get('page', 1))

    # page = request.args.get('page', default=1, type=int)
    # per = request.args.get('per', default=5, type=int)

    # start_idx = (page - 1) * per
    # end_idx = start_idx + per

# END
#
#
# В этой практике вам предстоит попрактиковаться в части READ операций CRUD.
# Обычно "чтение" предполагает вывод всей категории ресурсов(списка
# пользователей, постов, комментариев) и детальный вывод конкретного
# ресурса (личная страничка пользователя). Для удобства также используется
# пейджинг с переходами "вперед" и "назад".
# src/app.py
# Реализуйте следующие обработчики:
# Список постов: /posts
# Конкретный пост /posts/<slug > ,
# например, / posts/python-flask-crude-exercise
# Посты находятся в репозитории repo.
# Каждый пост содержит внутри себя четыре поля:
# id
# title — имя поста
# body — содержание поста
# slug — слаг
# Каждый пост из списка ведет на страницу конкретного поста.
# Список нужно вывести с пейджингом по пять постов на странице.
# На первой странице — первые пять постов, на второй — вторые пять и так далее.
# Переключение между страницами нужно сделать с помощью двух ссылок: назад
# и вперед. То, какая сейчас страница открыта, определяется параметром page.
# По умолчанию загружается первая страница.
# Страница конкретного поста отображает данные поста и позволяет вернуться
# на список. Если поста нет, то обработчик должен вернуть код ответа 404 и
# текст 'Page not found'.
# templates / posts / index.html
# Выведите список постов. Для каждого поста также нужно вывести ссылку,
# которая ведет на отображение — show. Ссылка представлена в виде слага.
# Не забудьте также добавить блок с переключением страниц.
# templates / posts / show.html
# Вывод информации о конкретном посте. Выводить только имя и содержимое поста.
# Подсказки
# Для реализации пейджинга понадобится извлечь все посты из репозитория
# с помощью метода content()
# Переход между страницами реализуется с помощью параметра запроса ?page =
# If Expresion
# Для поиска поста по slug используйте метод репозитория find()
