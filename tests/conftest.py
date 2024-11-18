import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def products():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def categories():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    ), Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def data_of_products():
    data = {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство коммуникации",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    }, {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром",
        "products": [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    }
    return data