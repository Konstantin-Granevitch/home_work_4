from src.product import LawnGrass, Product, Smartphone


def test_init_product(banana):
    """тест инициализации класса продуктов"""

    assert banana.name == "banana"
    assert banana.description == "fruit"
    assert banana.price == 150.35
    assert banana.quantity == 100


def test_repl_price(banana):
    """тест изменения цены продукта"""

    banana.price = 160.50
    assert banana.price == 160.50

    banana.price = 0
    assert banana.price == 160.50


def test_new_product():
    """тест на добавление продукта из словаря"""

    pinaple = {"name": "pinaple", "description": "fruit", "price": 250.50, "quantity": 20}
    obj_pinaple = Product.new_product(pinaple)

    assert obj_pinaple.name == "pinaple"


def test_str_product(banana):
    """тест вывода строки с описанием продукта"""

    assert str(banana) == "banana, 150.35 руб. Остаток: 100 шт."


def test_add_product(products):
    """тест проверки сложения продуктов"""

    assert products[0] + products[1] == 17436.08


def test_add_invalid_product():
    """тест проверки сложения товаров разных категорий"""

    smart = Smartphone("Honor", "hi-tec smartphone", 15900.90, 5, 90.1, "x8b", 256, "green")
    grass = LawnGrass("lounge", "beauty grass", 10000, 10, "china", "7 days", "green")

    try:
        sum_ = smart + grass
    except TypeError:
        er_message = "TypeError"

    assert er_message == "TypeError"


def test_print_mixin(capsys):
    """тест на вывод отладки через класс миксин"""

    prod_nokia = Product("nokia 5500", "smartphone", 5000, 5)
    pr_message = capsys.readouterr()

    assert pr_message.out.strip() == "Product('nokia 5500', 'smartphone', '5000', '5')"


def test_empty_product_quantity():
    """проверка на создание объекта с нулевым количеством"""

    try:
        empty_product = Product("empty", "nothing", 0, 0)
    except ValueError:
        empty_mesage = "отсутствуют продукты"

    assert empty_mesage == "отсутствуют продукты"
