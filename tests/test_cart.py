from shoppingcart.cart import ShoppingCart


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

def test_json_cart(cart_json: ShoppingCart):
   # Add an item that wasn't in the default items
   cart_json.add_item("orange", 2)

   receipt = cart_json.print_receipt()

   assert receipt[0] == "orange - 2 - €1.00"


def test_csv_cart(cart_csv: ShoppingCart):
   
  cart_csv.add_item("mango", 1 )
  
  receipt = cart_csv.print_receipt()

  assert receipt[0] == "mango - 1 - €1.50" 


def test_cart_total(cart: ShoppingCart):
  cart.add_item("apple", 2)
  cart.add_item("banana", 3)
  cart.add_item("kiwi", 1)
  
  receipt = cart.print_receipt()
  # Last line of the receipt should have the total
  assert cart._total_price == 8.3
  assert receipt[-1] == "Total - €8.30"
  
  # Add more apples to test count being updated
  cart.add_item("apple", 2)
  receipt = cart.print_receipt()
  
  assert cart._total_price == 10.3
  assert receipt[-1] == "Total - €10.30"

def test_usd_cart(cart_usd: ShoppingCart):
  cart_usd.add_item("apple", 2)
  
  receipt = cart_usd.print_receipt()
  assert receipt[0] == "apple - 2 - $2.24"

  assert receipt[-1] == "Total - $2.24"


def test_jpy_cart(cart_jpy: ShoppingCart):
  cart_jpy.add_item("banana", 2)
  cart_jpy.add_item("apple", 2)
  receipt = cart_jpy.print_receipt()
  expected_receipt = [
    "banana - 2 - ¥284.97",
    "apple - 2 - ¥259.06",
    "Total - ¥544.03"
  ]
  compare_receipts(expected_receipt, receipt)

def test_gbp_cart(cart_gbp: ShoppingCart): 
  cart_gbp.add_item("banana", 2)
  cart_gbp.add_item("apple", 2)
  receipt = cart_gbp.print_receipt()
  expected_receipt = [
    "banana - 2 - £1.89",
    "apple - 2 - £1.72",
    "Total - £3.61"
  ]

  compare_receipts(expected_receipt, receipt)