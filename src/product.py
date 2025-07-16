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

    def __str__(self):
        """метод пользовательского отображения данных о продукте"""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """метод для сложения продуктов и получения итоговой стоимости этих продуктов"""

        if type(self) is type(other):  # проверка на идентичность классов складываемых объектов
            summ = self.__price * self.quantity + other.__price * other.quantity
            return summ
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data, list_product=None):
        """метод для создания объекта класса из словаря"""

        # проверка на наличие списка продуктов
        if list_product is None:
            return cls(
                product_data["name"], product_data["description"], product_data["price"], product_data["quantity"]
            )

        # проверка на наличие схожего товара в списке товаров для избежания дублирования
        repl = False  # флаг для проверки был ли схожий товар в списке
        for product in list_product:
            if product_data["name"] in product.name:
                repl = True
                product.quantity += product_data["quantity"]
                if product_data["price"] > product.price:
                    product.price = product_data["price"]

        # вывод результата в зависимости от флага
        if repl:
            return None
        else:
            return list_product.append(
                cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])
            )

    @property
    def price(self):
        """метод-геттер для просмотра цены продукта"""

        return self.__price

    @price.setter
    def price(self, new_price):
        """метод-сеттер для изменения цены продукта"""

        if 0 < new_price < self.__price:
            # запрос у пользователя на подтверждение снижения цены
            user_answer = input("Подтвердите снижение цены 'y/n'\n")

            if user_answer.lower() == "y":
                self.__price = new_price

        elif new_price > self.__price:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    """
    класс смартфон принимает строки с именем и описанием и числовые значения с ценой и количеством,
    является подклассом класса продукт
    """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    класс газон принимает строки с именем и описанием и числовые значения с ценой и количеством,
    является подклассом класса продукт
    """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    new_prod = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    list_product = [product1, product2, product3]

    product4 = Product.new_product(new_prod, list_product)

    print(list_product[-1].quantity)
    print(product1)
    print(product1 + product2)
