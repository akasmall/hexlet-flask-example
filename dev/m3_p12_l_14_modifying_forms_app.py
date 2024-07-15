import os
from flask import Flask, redirect, render_template, request
# BEGIN (write your solution here)
from dev.m3_p12_l_14_modifying_forms_validator import validate
# END
from dev.m3_p12_l_14_modifying_forms_data import Repository


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
    )


# BEGIN (write your solution here)
@app.post('/courses')
def courses_post():
    courses = request.form.to_dict()
    errors = validate(courses)
    if errors:
        return render_template(
            'courses/new.html',
            courses=courses,
            errors=errors,
        ), 422
    if courses['paid'] == "1":
        courses['paid'] = True
    elif courses['paid'] == "0":
        courses['paid'] = False
    repo.save(courses)
    return redirect('/courses', code=302)


@app.get('/courses/new')
def courses_new():
    errors = {}
    courses = request.form.to_dict()

    return render_template(
        'courses/new.html',
        courses=courses,
        errors=errors,
    )

# END

# # решение ментора
# # BEGIN
# @app.post('/courses')
# def courses_post():
#     course = request.form.to_dict()
#     errors = validate(course)
#     if errors:
#         return render_template(
#             'courses/new.html',
#             course=course,
#             errors=errors,
#         ), 422

#     repo.save(course)
#     return redirect('/courses', 302)


# @app.route('/courses/new')
# def courses_new():
#     course = {'title': '', 'paid': ''}
#     errors = {}
#     return render_template(
#         'courses/new.html',
#         course=course,
#         errors=errors,
#     )
# # END
