# Create a list called menu, which should contain at least four items sold in the cafe.
menu = ["Espresso", "Macchiato", "Cappuccino", "Tea"]

# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
stock = {"Espresso": 100, "Macchiato": 80, "Cappuccino": 50, "Tea": 20}

# Create another dictionary called price, which should contain the prices for each item on your menu.
price = {"Espresso": 2.50, "Macchiato": 3.00, "Cappuccino": 4.00, "Tea": 1.50}

# Next, calculate the total_stock worth in the cafe.
#Empty string; is going to store my updated string
total_stock_worth = 0

#Loop through the dictionaries and lists
#I want to calculate the total_stock worth in the cafe
# so I have to calculate each ‘item_value’ by multiplying the stock value by the price value
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Finally, print out the result of your calculation
# Output the total_stock worth
print(f"The total stock worth in the cafe is: £{total_stock_worth}")
