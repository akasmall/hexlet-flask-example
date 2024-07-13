import random
from flask import Flask, render_template, request
from faker import Faker
# from data import generate_users

SEED = 1234


def generate_users(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(1, users_count))
    random.seed(SEED)
    random.shuffle(ids)

    users_ = []

    for i in range(users_count - 1):
        users_.append({
            'id': ids[i],
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.free_email(),
        })

    return users_


users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    result = users
    term = request.args.get('term', '')
    if term is not None:
        result = list(filter(
            lambda user: user['first_name'].lower().startswith(term.lower()),
            users
        ))
    return render_template(
        'users/index.html',
        users=result,
        search=term
    )
# END


# # решение ментора
# # BEGIN


# @app.route('/users')
# def get_users():
#     result = users
#     search = request.args.get('term', '')
#     if search:
#         result = [user for user in users if filter_name(user, search)]

#     return render_template(
#         'users/index.html',
#         users=result,
#         search=search,
#     )


# def filter_name(user, search):
#     return user['first_name'].lower().startswith(search.lower())
# # END
