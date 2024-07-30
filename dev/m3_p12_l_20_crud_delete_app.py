import os
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

from dev.m3_p12_l_20_crud_delete_repository import PostsRepository
from dev.m3_p12_l_20_crud_delete_validator import validate
# from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['SECRET_KEY'] = "SuperSecretKey"


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


@app.route('/posts/<id_>/update', methods=['GET', 'POST'])
def post_update(id_):
    repo = PostsRepository()
    post = repo.find(id_)
    errors = []

    if request.method == 'GET':
        return render_template(
            'posts/edit.html',
            post=post,
            errors=errors,
            data=post,
        )

    if request.method == 'POST':
        data = request.form.to_dict()

        errors = validate(data)
        if errors:
            return render_template(
                'posts/edit.html',
                post=post,
                data=data,
                errors=errors,
            ), 422

        post['title'] = data['title']
        post['body'] = data['body']
        repo.save(post)
        flash('Post has been updated', 'success')
        return redirect(url_for('posts_get'))


# BEGIN (write your solution here)
@app.route('/posts/<id_>/delete', methods=['GET', 'POST'])
def delete_post(id_):
    if request.method == 'POST':
        repo = PostsRepository()
        repo.destroy(id_)
        flash('Post has been removed', 'success')

        return redirect(url_for('posts_get'))
    else:
        return '', 405

# END
