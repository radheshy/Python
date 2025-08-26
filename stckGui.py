import requests
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import csv

API_KEY = "FSLB7P2LXNSTKJRD"   # Replace with your Alpha Vantage API key
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
        return None

    data = response.json()
    if "Time Series (Daily)" not in data:
        return None

    return data["Time Series (Daily)"]


def moving_average(values, window=10):
    """Compute simple moving average"""
    ma = []
    for i in range(len(values)):
        if i < window - 1:
            ma.append(None)
        else:
            window_slice = values[i - window + 1 : i + 1]
            avg = sum(window_slice) / window
            ma.append(avg)
    return ma


def save_to_csv(symbol, dates, closes, ma10):
    """Save stock data to CSV file"""
    filename = f"{symbol}_stock_data.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Close", "MA10"])
        for d, c, m in zip(dates, closes, ma10):
            writer.writerow([d, c, m if m else ""])
    return filename


def plot_stock(symbol, data):
    """Plot stock price and MA10"""
    dates = list(data.keys())[:30]  # last 30 days
    dates.reverse()
    closes = [float(data[d]["4. close"]) for d in dates]
    ma10 = moving_average(closes, 10)

    # Save to CSV
    filename = save_to_csv(symbol, dates, closes, ma10)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, closes, marker="o", label=f"{symbol.upper()} Price")
    plt.plot(dates, ma10, linestyle="--", label=f"{symbol.upper()} MA10")
    plt.title(f"{symbol.upper()} Stock Price with MA10 (Last 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return filename


# ------------------- GUI -------------------

def fetch_and_plot():
    symbols = entry.get().strip().split(",")
    if not symbols:
        messagebox.showerror("Error", "Please enter at least one stock symbol")
        return

    for symbol in symbols:
        symbol = symbol.strip().upper()
        data = get_stock_data(symbol)
        if not data:
            messagebox.showerror("Error", f"Could not fetch data for {symbol}")
            continue

        filename = plot_stock(symbol, data)
        messagebox.showinfo("Success", f"Data for {symbol} saved to {filename}")


root = tk.Tk()
root.title("📈 Stock Tracker with MA + CSV")
root.geometry("400x150")

label = tk.Label(root, text="Enter Stock Symbols (comma separated):")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="Fetch & Plot", command=fetch_and_plot)
btn.pack(pady=10)

root.mainloop()
