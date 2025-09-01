#for fetching stock prices
import yfinance as yf
class stock_porfolio:
    def __init__(self):
        self.portfolio={}
    def add_stock(self,ticker,quantity,buy_price):
        """add a stock to the portfolio"""
        self.portfolio[ticker]={'quantity':quantity,'buy_price':buy_price}
        print(f"'{ticker}' added to portfolio.")
    def remove_stock(self,ticker):
        """remove a stock from the portfolio"""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"'{ticker}' removed from portfolio.")
        else:
            print(f"{ticker} not found in portfolio.")
    def fetch_stock_price(self,ticker):
        """fetch real-time stock prices"""
        try:
            stock=yf.Ticker(ticker)
            return stock.history(period='1d')['Close'].iloc[-1] #get the closing price
        except Exception as e:
            print(f"Error fetching stock price for {ticker}:{e}")
            return None
    def show_portfolio(self):
        """Display portfolio with real-time updates."""
        total_value = 0
        print("\nStock Portfolio:")
        print("Ticker | Quantity | Buy Price | Current Price | Profit/Loss")
        print("-" * 60)

        for ticker, data in self.portfolio.items():
            current_price = self.fetch_stock_price(ticker)
            if current_price:
                investment_value = data["quantity"] * current_price
                profit_loss = (current_price - data["buy_price"]) * data["quantity"]
                total_value += investment_value

                print(
                    f"{ticker:6} | {data['quantity']:8} | ${data['buy_price']:9} | ${current_price:13.2f} | ${profit_loss:10.2f}"
                )
            else:
                print(f"{ticker} - Unable to fetch price.")
        print("-" * 60)
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
def main():
    portfolio=stock_porfolio()
    while True:
        print('''
        Stock Portfolio Ticker
        1.Add Stock
        2.Remove Stock
        3.View Portfolio
        4.Exit
        ''')
        choice =input('Choose an option:')
        if choice == '1':
            ticker = input('Enter stock ticker(e.g,.AAPL):').upper()
            quantity = int(input('Enter quantity:'))
            buy_price = float(input('Enter buy price per share:'))
            portfolio.add_stock(ticker,quantity,buy_price)
        elif choice == '2':
            ticker= input('Enter stock ticker to remove:').upper()
            portfolio.remove_stock(ticker)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            print('Exiting program .Goodbye!')
            break
        else:
            print('Invalid option.Please choose again.')
if __name__ == '__main__':
    main()


