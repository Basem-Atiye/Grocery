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

cart={}
user_input = ""
total_price = 0
while user_input != "done":
    user_input = input("Enter an item to check its price (or 'done' to exit): ")
    if user_input == "done":
        print("Thank you for shopping with us!")
        print("Your cart:", cart)
        print("Total price: $", total_price)
        break
    elif user_input in groceries:
        print(f"The price of {user_input} is ${groceries[user_input]}.")
        cart[user_input] = groceries[user_input]
        total_price += groceries[user_input]
    else:
        print(f"Sorry, {user_input} is not available in the grocery list.")