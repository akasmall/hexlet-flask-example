import json
import sys
import uuid
from flask import session


class PostsRepository():
    def __init__(self):
        if 'posts' not in session:
            session['posts'] = {}

    def content(self):
        return session['posts'].values()

    def find(self, id_):
        try:
            return session['posts'][id_]
        except KeyError:
            sys.stderr.write(f'Wrong post id: {id_}')
            raise

    def destroy(self, id_):
        del session['posts'][id_]

    def save(self, post):
        if not (post.get('title') and post.get('body')):
            raise Exception(f'Wrong data: {json.loads(post)}')
        if not post.get('id'):
            post['id'] = str(uuid.uuid4())
        session['posts'][post['id']] = post
        session['posts'] = session['posts']
