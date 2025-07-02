class Product:
    """класс продукт принимает строки с именем и описанием и числовые значения с ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        Product.name = name
        Product.description = description
        Product.price = price
        Product.quantity = quantity
