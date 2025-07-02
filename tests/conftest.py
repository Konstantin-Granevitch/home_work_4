import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def banana():
    return Product("banana", "fruit", 150.35, 100)


@pytest.fixture
def fruits():
    return Category("fruits", "sweet fruits", ["banana", "aple", "orange"])
