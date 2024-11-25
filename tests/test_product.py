from unittest.mock import patch

from src.product import Product


def test_product(products):
    assert products.name == "Samsung Galaxy C23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_sample_product(products):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 185000.0,
            "quantity": 5,
        }
    )

    assert new_product.name == "Samsung Galaxy C23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 185000.0
    assert new_product.quantity == 10


def test_new_product():
    new_product_2 = Product.new_product(
        {"name": '55" QLED 5K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    )

    assert new_product_2.name == '55" QLED 5K'
    assert new_product_2.description == "Фоновая подсветка"
    assert new_product_2.price == 123000
    assert new_product_2.quantity == 7


def test_invalid_price(products, capsys):
    products.price = 0
    captured = capsys.readouterr()

    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert products.price == 180000.0


@patch("builtins.input", return_value="y")
def test_price_changes_on_lower_value_with_confirmation(mock_input, products):
    products.price = 170000.0
    assert products.price == 170000.0  # Цена изменилась


@patch("builtins.input", return_value="n")
def test_price_not_changed_on_lower_value_without_confirmation(mock_input, products):
    products.price = 170000.0
    assert products.price == 180000.0  # Цена не изменилась


def test_normal_price(products, capsys):
    products.price = 200000.0

    captured = capsys.readouterr()
    assert captured.out == ""
    assert products.price == 200000.0


def test_add_method(add_products):
    result_1 = add_products[0] + add_products[1]
    assert result_1 == 2580000.0

    result_2 = add_products[0] + add_products[2]
    assert result_2 == 1334000.0

    result_3 = add_products[1] + add_products[2]
    assert result_3 == 2114000.0
