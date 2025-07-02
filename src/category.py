class Category:
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
