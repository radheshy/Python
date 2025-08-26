import requests
import matplotlib.pyplot as plt

API_KEY = "FSLB7P2LXNSTKJRD"  # Replace with your key
BASE_URL = "https://www.alphavantage.co/query"


def get_stock_data(symbol):
    """Fetch daily stock data for a given symbol"""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"⚠ API request failed for {symbol}")
        return None

    data = response.json()
    if "Time Series (Daily)" not in data:
        print(f"⚠ Could not fetch data for {symbol}. Check symbol or API key.")
        return None

    return data["Time Series (Daily)"]


def plot_multiple_stocks(stock_data_dict):
    """Plot multiple stocks on one chart"""
    plt.figure(figsize=(12, 6))

    for symbol, data in stock_data_dict.items():
        if not data:
            continue
        dates = list(data.keys())[:30]  # last 30 days
        dates.reverse()
        closes = [float(data[date]["4. close"]) for date in dates]
        plt.plot(dates, closes, marker="o", label=symbol.upper())

    plt.title("📈 Stock Price Comparison (Last 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    print("=== 📈 Multi-Stock Tracker ===")
    print("Enter stock symbols separated by commas (e.g., AAPL,MSFT,TSLA)")
    symbols = input("Stocks: ").strip().split(",")

    stock_data_dict = {}
    for symbol in symbols:
        symbol = symbol.strip().upper()
        if symbol:
            print(f"Fetching {symbol}...")
            data = get_stock_data(symbol)
            stock_data_dict[symbol] = data

    if stock_data_dict:
        plot_multiple_stocks(stock_data_dict)


if __name__ == "__main__":
    main()
