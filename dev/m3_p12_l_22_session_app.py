import os
from hashlib import sha256
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


users = [
    {'name': 'tota', 'password': sha256(b'password123').hexdigest()},
    {'name': 'alice', 'password': sha256(b'donthackme').hexdigest()},
    {'name': 'bob', 'password': sha256(b'qwerty').hexdigest()},
]


def get_user(form_data, repo):
    name = form_data['name']
    password = sha256(form_data['password'].encode()).hexdigest()
    for user in repo:
        if user['name'] == name and user['password'] == password:
            return user


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    current_user = session.get('user')
    return render_template(
        'index.html',
        messages=messages,
        current_user=current_user,
    )


# BEGIN (write your solution here)
@app.route('/session/new', methods=["POST"])
def session_new():
    if 'user' not in session:
        session['user'] = {}
    user = get_user(request.form, users)
    if user is None:
        flash('Wrong password or name.', 'error')
        return redirect(url_for('index'), )
    session['user'].update(user)
    return redirect(url_for('index'))


@app.route('/session/delete', methods=["POST", "DELETE"])
def session_delete():
    session.clear()
    return redirect(url_for('index'))

# END

# !Многие действия на сайтах допустимы только для аутентифицированных
# пользователей: оформление заказа, редактирование профиля,
# добавление в подписки.

# ?В этой практике необходимо реализовать систему аутентификации.
# ?В простом случае она состоит из двух маршрутов:

# *POST /session/new — создает сессию
# *POST, DELETE /session/delete — удаляет сессию
# *После выполнения каждого из этих действий происходит редирект на главную.

# !scr / app.py
# *Реализуйте указанные выше маршруты. Список пользователей с именами
# *и паролями доступен в списке users. Чтобы получить пользователя,
# *используйте функцию get_user().

# *Если имя или пароль неверные, то происходит редирект на главную,
# *и показывается флеш сообщение Wrong password or name.


# !решение ментора
# ?# BEGIN
# *@app.route('/session/new', methods=['POST'])
# *def session_new():
#     user_data = request.form.to_dict()
#     current_user = get_user(user_data, users)
#     if current_user:
#         session['user'] = current_user
#     else:
#         flash('Wrong name or password')
#     return redirect(url_for('index'))


# *@app.route('/session/delete', methods=['POST', 'DELETE'])
# *def session_delete():
#     session.pop('user')
#     return redirect(url_for('index'))
# ?# END
