from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_index():
    return 'open something like (you can change id): /users/5'


# @app.route('/users/<id_>')
# def get_users(id_):
#     res = render_template(
#         'index.html',
#         name=id_,
#     )
#     return res


@app.route('/users/<id_>')
def get_users(id_):
    res = render_template(
        'users/show.html',
        name=id_,
    )
    return res


if __name__ == '__main__':
    app.run()
