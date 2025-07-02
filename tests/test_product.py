def test_init_product(banana):
    assert banana.name == "banana"
    assert banana.description == "fruit"
    assert banana.price == 150.35
    assert banana.quantity == 100
