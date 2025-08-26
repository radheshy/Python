import requests
import matplotlib.pyplot as plt

API_KEY = "FSLB7P2LXNSTKJRD"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol):
    """Fetch daily stock data"""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("⚠ API request failed!")
        return None

    data = response.json()
    if "Time Series (Daily)" not in data:
        print("⚠ Could not fetch data. Check symbol or API key.")
        return None

    return data["Time Series (Daily)"]


def plot_stock(data, symbol):
    """Plot stock closing prices"""
    dates = list(data.keys())[:30]  # last 30 days
    dates.reverse()  # oldest to latest
    closes = [float(data[date]["4. close"]) for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, closes, marker="o")
    plt.title(f"Stock Prices for {symbol.upper()} (Last 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    print("=== 📈 Stock Price Tracker ===")
    while True:
        symbol = input("\nEnter stock symbol (or 'exit' to quit): ").strip()
        if symbol.lower() == "exit":
            print("👋 Goodbye!")
            break

        data = get_stock_data(symbol)
        if data:
            # print latest info
            latest_date = sorted(data.keys())[0]
            latest = data[latest_date]
            print(f"\nLatest ({latest_date})")
            print(f"Open: {latest['1. open']}")
            print(f"High: {latest['2. high']}")
            print(f"Low: {latest['3. low']}")
            print(f"Close: {latest['4. close']}")
            print(f"Volume: {latest['5. volume']}")

            # plot chart
            plot_stock(data, symbol)


if __name__ == "__main__":
    main()