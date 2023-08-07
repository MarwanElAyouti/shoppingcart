from shoppingcart.cart import ShoppingCart
import pytest


@pytest.fixture
def cart() -> ShoppingCart:
  return ShoppingCart()


def compare_receipts(expected_receipt, receipt):
    # Compare the order of items in the generated receipt with the expected order
    # Tests that the shopping cart print_receipt prints items in the order that they were added.
    for expected_item, actual_item in zip(expected_receipt, receipt):
        assert expected_item == actual_item


def test_add_item(cart: ShoppingCart):
  cart.add_item("apple", 1)

  receipt = cart.print_receipt()

  assert receipt[0] == "apple - 1 - €1.00"


def test_add_item_with_multiple_quantity(cart: ShoppingCart):
  cart.add_item("apple", 2)

  receipt = cart.print_receipt()

  assert receipt[0] == "apple - 2 - €2.00"


def test_add_different_items(cart: ShoppingCart):
  cart.add_item("banana", 1)
  cart.add_item("kiwi", 1)

  receipt = cart.print_receipt()

  assert receipt[0] == "banana - 1 - €1.10"
  assert receipt[1] == "kiwi - 1 - €3.00"

def test_print_receipt_order(cart: ShoppingCart):
    # Add items to the cart in a specific order
    cart.add_item("banana", 3)
    cart.add_item("kiwi", 1)
    cart.add_item("apple", 2)
    # Generate the receipt
    receipt = cart.print_receipt()

    # Expected order of items in the receipt
    expected_receipt_order = [
        "banana - 3 - €3.30",
        "kiwi - 1 - €3.00",
        "apple - 2 - €2.00",
    ]
    compare_receipts(expected_receipt_order, receipt)