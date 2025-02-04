import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download stock data from Yahoo Finance
def get_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock

# Plot stock closing price and moving averages
def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data["Close"], label="Closing Price", linewidth=2)
    plt.plot(stock_data["Close"].rolling(window=20).mean(), label="20-Day MA", linestyle="dashed")
    plt.plot(stock_data["Close"].rolling(window=50).mean(), label="50-Day MA", linestyle="dotted")
    
    plt.title(f"{ticker} Stock Price & Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

# Main execution
if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA, GOOG): ").upper()
    start_date = "2023-01-01"
    end_date = "2024-01-01"

    stock_data = get_stock_data(ticker, start_date, end_date)

    if not stock_data.empty:
        print(stock_data.head())  # Print first few rows
        plot_stock_data(stock_data, ticker)
    else:
        print("No data found for the given ticker.")
