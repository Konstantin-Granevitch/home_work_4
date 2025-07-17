import json
from pprint import pprint

from config import BASE_PATH
from src.category import Category
from src.product import Product


def json_class_creator(json_file: str) -> object:
    """
    функция для чтения данных из json файлов и создания объектов класса
    """

    with open(f"{BASE_PATH}/data/{json_file}") as f:
        list_data = json.load(f)

    list_category_class = []
    list_product_class = []

    for obj in list_data:
        category = Category(obj["name"], obj["description"], obj["products"])
        list_category_class.append(category)

        for item in obj["products"]:
            product = Product(item["name"], item["description"], item["price"], item["quantity"])
            list_product_class.append(product)

    return list_category_class, list_product_class


if __name__ == "__main__":
    pprint(json_class_creator("products.json"))
