from src.category import Category


def test_init_category(fruits):
    """тестирование инициализации категорий"""

    assert fruits.name == "fruits"
    assert fruits.description == "sweet fruits"
    assert fruits.category_count == 1
    assert fruits.product_count == 3


def test_add_product_in_category(products):
    """тестирование добавления продуктов"""

    categ1 = Category("fruit", "sweet fruits", products)

    assert categ1.product_count == 5


def test_view_products_in_category(fruits):
    """тестирование вывода списка продуктов и их цен"""

    assert (
        fruits.products
        == """orange, 99.9 руб., Остаток: 50 шт.\n\
banana, 150.79 руб., Остаток: 45 шт.\naple, 95.99 руб., Остаток: 100 шт.\n"""
    )
