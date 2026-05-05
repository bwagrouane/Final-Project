from decimal import Decimal


def calculate_order_total(items):
    total = Decimal("0.00")

    for item in items:
        total += Decimal(str(item["price"])) * item["quantity"]

    return total


def test_order_total_one_item():
    items = [
        {
            "price": 5.00,
            "quantity": 2
        }
    ]

    total = calculate_order_total(items)

    assert total == Decimal("10.00")


def test_order_total_multiple_items():
    items = [
        {
            "price": 5.00,
            "quantity": 2
        },
        {
            "price": 2.50,
            "quantity": 3
        }
    ]

    total = calculate_order_total(items)

    assert total == Decimal("17.50")


def test_order_total_zero_items():
    items = []

    total = calculate_order_total(items)

    assert total == Decimal("0.00") 