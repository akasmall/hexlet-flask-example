import random
from faker import Faker
from flask import Flask, jsonify, request
# from data import generate_companies

SEED = 1234


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)
    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)
    companies_ = []
    for _ in range(companies_count):
        companies_.append({
            "name": fake.company(),
            "phone": fake.phone_number(),
        })
    return companies_


companies = generate_companies(100)

app = Flask(__name__)
# app.config['TESTING'] = True
# app.run(debug=True, use_debugger=False, use_reloader=False)


@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"


# BEGIN (write your solution here)
@app.route('/companies')
def get_companies():
    page = request.args.get('page', default=1, type=int)
    per = request.args.get('per', default=5, type=int)

    start_idx = (page - 1) * per
    end_idx = start_idx + per
    companies_on_page = companies[start_idx:end_idx]

    return jsonify(companies_on_page)

# END
