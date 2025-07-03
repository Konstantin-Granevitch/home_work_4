def test_init_category(fruits):
    assert fruits.name == "fruits"
    assert fruits.description == "sweet fruits"
    assert fruits.category_count == 1
    assert fruits.product_count == 3
