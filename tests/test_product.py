from src.product import Product


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
