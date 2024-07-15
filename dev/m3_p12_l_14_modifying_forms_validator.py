def validate(courses):
    errors = {}
    if not courses['title']:
        errors['title'] = "Can't be blank"
    if not courses['paid'] or courses['paid'] not in ["1", "0"]:
        errors['paid'] = "Can't be blank"
    return errors

# # решение ментора
# # BEGIN
# def validate(course):
#     errors = {}
#     if not course.get('title'):
#         errors['title'] = "Can't be blank"
#     if not course.get('paid'):
#         errors['paid'] = "Can't be blank"
#     return errors
# # END
