from src.category import Category
from src.product import Product


class Iterator:
    """класс - итератор для прохода по объектам других классов"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.category.product_count:
            result = self.category.products.splitlines()[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    prod1 = Product("orange", "fruit", 99.90, 50)
    prod2 = Product("banana", "fruit", 150.79, 45)
    prod3 = Product("aple", "fruit", 95.99, 100)
    prod4 = Product("pear", "fruit", 130.99, 92)
    categ1 = Category("fruit", "sweet fruits", [prod1, prod2, prod3, prod4])

    iter_category = Iterator(categ1)

    for product in iter_category:
        print(product)
