
#### Overview
This report provides an analysis of the **Stock Portfolio Management System** implemented in Python. The system allows users to manage a stock portfolio by adding, removing, and viewing stocks with real-time price updates. The system uses the `yfinance` library to fetch real-time stock prices.

---

### Key Features
1. **Add Stock**: Users can add a stock to the portfolio by providing the stock ticker, quantity, and buy price.
2. **Remove Stock**: Users can remove a stock from the portfolio by specifying the stock ticker.
3. **View Portfolio**: Displays the current portfolio with real-time stock prices, investment value, and profit/loss calculations.
4. **Real-Time Price Updates**: Fetches the latest stock prices using the `yfinance` library.
5. **Interactive Menu**: Provides a user-friendly command-line interface for managing the portfolio.

---

### Code Structure
The code is organized into a class `stock_porfolio` with the following methods:

1. **`__init__`**: Initializes an empty portfolio dictionary.
2. **`add_stock`**: Adds a stock to the portfolio with its ticker, quantity, and buy price.
3. **`remove_stock`**: Removes a stock from the portfolio by its ticker.
4. **`fetch_stock_price`**: Fetches the real-time stock price using the `yfinance` library.
5. **`show_portfolio`**: Displays the portfolio with real-time updates, including current prices, investment value, and profit/loss.
6. **`main`**: Provides an interactive menu for users to manage the portfolio.

---

### Example Workflow
1. **Add a Stock**:
   - User selects option `1` from the menu.
   - Enters the stock ticker (e.g., `AAPL`), quantity (e.g., `10`), and buy price (e.g., `150`).
   - The stock is added to the portfolio.

2. **Remove a Stock**:
   - User selects option `2` from the menu.
   - Enters the stock ticker to remove (e.g., `AAPL`).
   - The stock is removed from the portfolio.

3. **View Portfolio**:
   - User selects option `3` from the menu.
   - The system displays the portfolio with real-time stock prices, investment value, and profit/loss.

4. **Exit**:
   - User selects option `4` to exit the program.

---

### Sample Output
#### Adding a Stock:
```
Enter stock ticker (e.g., AAPL): AAPL
Enter quantity: 10
Enter buy price per share: 150
'AAPL' added to portfolio.
```

#### Viewing Portfolio:
```
Stock Portfolio:
Ticker | Quantity | Buy Price | Current Price | Profit/Loss
------------------------------------------------------------
AAPL   |       10 | $     150 | $       160.50 | $     105.00
------------------------------------------------------------

Total Portfolio Value: $1605.00
```

#### Removing a Stock:
```
Enter stock ticker to remove: AAPL
'AAPL' removed from portfolio.
```

---

### Limitations
1. **Error Handling**: The system does not handle all edge cases, such as invalid ticker symbols or network errors while fetching stock prices.
2. **Data Persistence**: The portfolio data is not saved between program runs. It is lost when the program exits.
3. **Real-Time Updates**: The stock prices are fetched only when the portfolio is viewed, not in real-time.

---

### Recommendations for Improvement
1. **Data Persistence**: Implement a database or file storage system to save the portfolio data between program runs.
2. **Enhanced Error Handling**: Add robust error handling for invalid inputs, network errors, and API failures.
3. **Real-Time Updates**: Use a background process or scheduler to fetch stock prices periodically and update the portfolio in real-time.
4. **User Authentication**: Add user authentication to allow multiple users to manage their own portfolios.
5. **Graphical User Interface (GUI)**: Develop a GUI for a more user-friendly experience.

---

### Conclusion
The **Stock Portfolio Management System** is a functional tool for managing a stock portfolio with real-time price updates. It provides a simple and interactive interface for users to add, remove, and view stocks. With further enhancements, such as data persistence and improved error handling, the system can be made more robust and user-friendly.

---
