# week5_lab.py
# Author: Anant Gaan
# Business domain: Event Catering

item_name = "boxed lunch"
status = "pending"
quantity = 30
unit_price = 45.00
is_over_limit = unit_price * quantity > 1000

print(type(item_name), type(quantity), type(unit_price), type(is_over_limit))

subtotal = quantity * unit_price
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000
print("=== Catering Order Summary ===")
print(f"Item: {item_name}")
print(f"Status: {status}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Requires Approval: {requires_approval}")

# Part 3: User Input
user_qty = int(input("Enter a new quantity: "))
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} {item_name}(s) is: ${new_total:.2f}")
print(f"Requires Approval: {new_total > 1000}")
