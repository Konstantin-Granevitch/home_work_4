class Category:
    """
    класс категория принимает строки с именем и описанием и список с продуктами и автоматически подсчитывает
    количество категорий и продуктов в них
    """

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        Category.name = name
        Category.description = description
        Category.products = products

        Category.category_count += 1
        Category.product_count += len(Category.products)
