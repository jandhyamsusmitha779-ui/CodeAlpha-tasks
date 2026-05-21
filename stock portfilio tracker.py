stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 130
}

total = 0

print("Stock Portfolio Tracker")

stock_name = input("Enter stock name: ").upper()

if stock_name in stocks:
    quantity = int(input("Enter quantity: "))

    total = stocks[stock_name] * quantity

    print("Total Investment Value:", total)

    file = open("portfolio.txt", "w")
    file.write(f"Stock: {stock_name}\n")
    file.write(f"Quantity: {quantity}\n")
    file.write(f"Total Value: {total}")
    file.close()

    print("Data saved in portfolio.txt")

else:
    print("Stock not found!")