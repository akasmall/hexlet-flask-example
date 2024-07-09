import random
from faker import Faker
from flask import Flask, render_template


SEED = 1234


def generate_users(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(1, users_count))
    random.seed(SEED)
    random.shuffle(ids)

    users = []

    for i in range(users_count - 1):
        users.append({
            'id': ids[i],
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.free_email(),
        })

    return users


users_dct = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    return render_template(
        '/users/index.html',
        users=users_dct
    )


@app.route('/users/<user_id>')
def get_user(user_id):
    current_user = list(filter(lambda x: x['id'] == int(user_id), users_dct))
    if len(current_user) > 0:
        res = render_template(
            '/users/show.html',
            name=user_id,
            user=current_user[0]
        )
    else:
        res = "Page not found", 404

    return res
# END

# решение ментора
# BEGIN
# @app.route('/users/<int:id>')
# def get_user(id):
#     filtered_users = filter(lambda user: user['id'] == id, users)
#     user = next(filtered_users, None)

#     if user is None:
#         return 'Page not found', 404

#     return render_template('users/show.html', user=user)


# @app.route('/users')
# def get_users():
#     return render_template('users/index.html', users=users)
# END
