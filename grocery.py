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
    "blueberries": 9
}

n=len(groceries)
for i in range (n):
    item=list(groceries.keys())[i]
    price=groceries[item]
    print(f"{item}: ${price}")

cart={}
user_input = ""
total_price = 0
while user_input != "done":
    user_input = input("Enter an item to add to your cart (or 'done' to exit): ")
    if user_input == "done":
        print("Thank you for shopping with us!")
        print("Your cart:", cart)
        print("Total price: $", total_price)
        break
    elif user_input in groceries:
        cart[user_input] = groceries[user_input]
        total_price += groceries[user_input]
    else:
        print(f"Sorry, {user_input} is not available in the grocery list.")