import random
from flask import Flask, jsonify
from faker import Faker

SEED = 1234


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)

    companies_ = []

    for i in range(companies_count):
        companies_.append({
            "id": ids[i],
            "name": fake.company(),
            "phone": fake.phone_number(),
        })

    return companies_


companies = generate_companies(100)
app = Flask(__name__)


@app.route('/')
def index():
    return 'open something like (you can change id): /companies/5'


# @app.route('/companies/<company_id>')
# def get_companies(company_id):
#     int_id = int(company_id)
#     filter_data = list(filter(lambda x: x['id'] == int_id, companies))
#     if len(filter_data) > 0:
#         f_d_id = filter_data[0]['id']
#         f_d_name = filter_data[0]['name']
#         f_d_phone = filter_data[0]['phone']
#         res = jsonify({
#             "id": f_d_id,
#             "name": f_d_name,
#             "phone": f_d_phone
#         })
#         # res = {"id": filter_data[0]['id'], "name": filter_data[0]
#         #        ['name'], "phone": filter_data[0]['phone']}
#     else:
#         # return jsonify({'message': 'Page not found'}), 404
#         res = jsonify("Page not found"), 404

#     return res


@app.route('/companies/<company_id>')
def get_companies(company_id):
    current_company = [
        company for company in companies if int(company_id) == company['id']]
    if len(current_company):
        res = jsonify({
            "id": current_company[0]["id"],
            "name": current_company[0]["name"],
            "phone": current_company[0]["phone"]
        })
    else:
        res = "Page not found", 404

    return res
