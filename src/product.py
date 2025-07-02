class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        Product.name = name
        Product.description = description
        Product.price = price
        Product.quantity = quantity
