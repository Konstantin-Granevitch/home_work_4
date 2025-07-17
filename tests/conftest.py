import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def banana():
    return Product("banana", "fruit", 150.35, 100)


@pytest.fixture
def fruits():
    return Category(
        "fruits",
        "sweet fruits",
        [
            Product("orange", "fruit", 99.90, 50),
            Product("banana", "fruit", 150.79, 45),
            Product("aple", "fruit", 95.99, 100),
        ],
    )


@pytest.fixture
def products():
    prod1 = Product("pear", "fruit", 130.99, 92)
    prod2 = Product("mango", "fruit", 179.50, 30)

    return prod1, prod2
