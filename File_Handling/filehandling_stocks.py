import csv

# Open the CSV file containing stock data
with open("/home/avishek/Avishek/Python/stocks.csv", "r") as file:
    reader = csv.reader(file)

    # Skip header row if present
    header = next(reader)
    print("Header:", header)

    # Process each row
    for row in reader:
        # Assuming columns are: Date, Open, High, Low, Close, Volume
        date = row[0]
        open_price = float(row[1])
        close_price = float(row[4])

        # Calculate difference
        difference = close_price - open_price

        # Print status
        if difference > 0:
            print(f"{date}: Stock went UP by {difference:.2f} (Open: {open_price}, Close: {close_price})")
            suggestion = "This stock shows positive momentum. Suitable to consider buying."
        elif difference < 0:
            print(f"{date}: Stock went DOWN by {abs(difference):.2f} (Open: {open_price}, Close: {close_price})")
            suggestion = "This stock is declining. Be cautious before buying."
        else:
            print(f"{date}: No change in stock price (Open: {open_price}, Close: {close_price})")
            suggestion = "Neutral trend. Monitor before making a decision."

        # Print suggestion
        print("Suggestion:", suggestion)
        print("-" * 60)