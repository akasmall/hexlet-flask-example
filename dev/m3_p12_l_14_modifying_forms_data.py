import sys
import uuid
from flask import session


class Repository:
    def content(self):
        return session.values()

    def find(self, id_):
        try:
            return session[id_]
        except KeyError:
            sys.stderr.write(f'Wrong item id: {id_}')
            raise

    def save(self, item):
        item['id'] = str(uuid.uuid4())
        session[item['id']] = item
