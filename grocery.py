groceries = {
    "apples": 5,
    "bananas": 3,
    "oranges": 4,
    "grapes": 2,
    "pears": 6,
    "peaches": 7,
    "mangoes": 8,
    "kiwis": 4,
    "strawberries": 10,
    "blueberries": 9,
    "milk": 6
}

for item, price in groceries.items():
    print(f"{item}: ${price}")

cart = {}
total_price = 0
user_input = ""

while True:
    user_input = input("Enter an item and quantity (e.g. 'apple 3') or 'done' to exit: ").strip()
    
    if user_input == "done":
        print("\nThank you for shopping with us!")
        print("Your cart:", cart)

        final_price = 0
        for item, quantity in cart.items():
            price = groceries[item]
            if item == "milk" and quantity > 2:
                price = price-1  
            final_price += price * quantity
        
        print("Total price: $", final_price)
        break

    parts = user_input.split()
    if len(parts) != 2:
        print("Please enter in the format 'item quantity'.")
        continue

    item = parts[0]
    quantity_str = parts[1]
    if item not in groceries:
        print(f"Sorry, {item} is not available in the grocery list.")
        continue

    if item in cart:
        cart[item] += int(quantity_str)
    else:
        cart[item] = int(quantity_str)
