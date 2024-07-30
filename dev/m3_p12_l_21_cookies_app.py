import os
from flask import (
    Flask,
    json,
    redirect,
    render_template,
    request
)


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index.html', cart=cart)


# BEGIN (write your solution here)
@app.route('/cart-items', methods=['POST'])
def cart_items_add():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    data = request.form.to_dict()
    current_item = cart.get(data["item_id"], None)
    if current_item is None:
        cart.update(
            {
                data["item_id"]: {"name": data["item_name"], "count": 1}
            }
        )
    else:
        current_item["count"] += 1

    encoded_cart = json.dumps(cart)
    response = redirect('/')
    response.set_cookie('cart', encoded_cart)
    return response


@app.route('/cart-items/clean', methods=['POST'])
def cart_items_clean():
    encoded_cart = json.dumps({})
    response = redirect('/')
    response.set_cookie('cart', encoded_cart)
    return response

# END

# !Задание
# ?Чтобы отличить заказы одного пользователя от другого нужно привязать
# ?их к какому-то уникальному идентификатору. Для этого мы можем
# ?использовать механизм кук и хранить все данные заказа в браузере
# ?пользователя или как говорят, на клиенте.

# ?В этой практике вам нужно будет реализовать корзину сайта с двумя
# ?обработчиками ее содержимого.

# !src / app.py
# ?Реализуйте два обработчика:

# *POST / cart - items — для добавления товаров в корзину
# *POST / cart - items / clean — для очистки корзины

# ?Корзина должна быть представлена сериализованным в JSON словарем и
# ?храниться на клиенте в куках. В корзине нужно хранить наименование
# ?товара и его количество. Когда товар добавляется, это приводит к увеличению
# ?счетчика и редиректу на главную страницу. Если очистить корзину, это
# ?приведет к удалению всех товаров из корзины и также редиректу
# ?на главную страницу.

# !Структуру данных корзины можно посмотреть
# *в шаблоне src / templates / index.html.

# !Подсказки
# *Для сериализации / десериализации данных используйте
# *json.dumps() и json.loads()
# ? https://flask.palletsprojects.com/en/2.0.x/api/#flask.json.dumps
# *flask.redirect() возвращает объект ответа Response
# ? https://flask.palletsprojects.com/en/2.0.x/api/#flask.redirect
# *Работа с Cookies
# ? https://flask.palletsprojects.com/en/2.2.x/quickstart/#cookies
# *set_cookie()
# ? https://flask.palletsprojects.com/en/2.0.x/api/#flask.Response.set_cookie


# !решение ментора
# ?# BEGIN
# *@app.route('/cart-items', methods=['POST'])
# *def add_item_to_cart():
#     cart = json.loads(request.cookies.get('cart', json.dumps({})))

#     id = request.form['item_id']
#     name = request.form['item_name']

#     item = cart.setdefault(id, {'name': name, 'count': 0})
#     item['count'] += 1

#     encoded_cart = json.dumps(cart)

#     response = redirect('/')
#     response.set_cookie('cart', encoded_cart)

#     return response


# *@app.route('/cart-items/clean', methods=['POST'])
# *def clean_cart():
#     response = redirect('/')
#     response.delete_cookie('cart')

#     return response
# ?# END
