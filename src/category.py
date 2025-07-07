from src.product import Product


class Category:
    """
    класс категория принимает строки с именем и описанием и список с продуктами и автоматически подсчитывает
    количество категорий и продуктов в них
    """

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """метод инициализации"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """метод для просмотра приватного метода 'списка продуктов'"""

        list_products = ""

        for obj in self.__products:
            list_products += f"{obj.name}, {obj.price} руб., Остаток: {obj.quantity} шт.\n"

        return list_products

    def add_product(self, product):
        """метод добавления продукта"""

        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            print(f"объект {product} не является экземпляром класса 'Product', проверьте данные")


if __name__ == "__main__":
    prod1 = Product("orange", "fruit", 99.90, 50)
    prod2 = Product("banana", "fruit", 150.79, 45)
    prod3 = Product("aple", "fruit", 95.99, 100)
    prod4 = Product("pear", "fruit", 130.99, 92)
    categ1 = Category("fruit", "sweet fruits", [prod1, prod2, prod3, prod4])
    categ1.add_product(Product("pinaple", "fruit", 230.35, 21))
    categ1.add_product(("mango", "fruit", 190.40, 47))

    print(categ1.products)
    print(categ1.product_count)
