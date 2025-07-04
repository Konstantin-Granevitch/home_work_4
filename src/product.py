class Product:
    """класс продукт принимает строки с именем и описанием и числовые значения с ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """метод для создания объекта класса из словаря"""

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


if __name__ == "__main__":
    prod1 = {"name": "banana", "price": 100.25, "description": "fruit", "quantity": 100}
    obj1 = Product.new_product(prod1)
    print(obj1.name)
    print(obj1.price)

    obj1.price = 51.55
    print(obj1.price)

    obj1.price = -10
    print(obj1.price)
