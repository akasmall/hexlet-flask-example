# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from faker import Faker  # noqa: C0114
from flask import Flask, jsonify

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]

app = Flask(__name__)


@app.route('/')
def index():
    return 'go to the /phones or /domains'


# BEGIN (write your solution here)
@app.route('/domains')
def get_domains():  # noqa: C0116
    # data = {"domains": domains}
    return jsonify(domains)


@app.route('/phones')
def get_phones():
    # data = {"domains": phones}
    # res = jsonify(data)
    return jsonify(phones)

# END
