# average.py
# hw 2.3

# Enter the item name: banana
# Enter the number purchased: 100
# Enter the total price: 153

# The average price of a(n) banana is 1.53 dollars

itemName = input("Enter the item name: ")
itemCount = int(input("Enter the number purchased: "))
totalPrice = int(input("Enter the total price: "))
print()
avgPrice = totalPrice/itemCount
print(f"The average price of a(n) {itemName} is {avgPrice:.2f} dollars")
