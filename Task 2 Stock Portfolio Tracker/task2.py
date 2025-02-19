import requests

def get_stock_price(symbol):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url).json()
    return float(response["Global Quote"].get("05. price", 0))

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    
    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")
    
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] > shares:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}.")
            else:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
        else:
            print(f"{symbol} not found in portfolio.")
    
    def view_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            price = get_stock_price(symbol)
            total_value = price * shares
            print(f"{symbol}: {shares} shares | Current Price: ${price:.2f} | Total Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
