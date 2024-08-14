# src/data_api_client.py

"""
data_api_client.py - A client for interacting with various financial and data APIs.

This module provides a class, `DataAPIClient`, that encapsulates the functionality required
to interact with various data sources like Yahoo Finance, Forex rates, and others. It includes
methods for fetching market data, exchange rates, and other relevant information.

Key Features of the `DataAPIClient` class:
    - Initialization (`__init__` method):
        - Sets up API keys and initializes connection parameters.
    - Yahoo Finance API (`get_stock_data` method):
        - Fetches historical stock data and returns it in a pandas DataFrame.
    - Forex API (`get_forex_rate` method):
        - Retrieves the current exchange rate between two currencies.
    - Cryptocurrency API (`get_crypto_data` method):
        - Fetches historical cryptocurrency data and returns it in a pandas DataFrame.
    - Error Handling:
        - Methods are wrapped in try-except blocks for robust error handling.

Usage Example:
    from data_api_client import DataAPIClient

    # Initialize the API client
    client = DataAPIClient()

    # Fetch stock data
    df = client.get_stock_data("AAPL", start="2023-01-01", end="2023-06-30")
    print(df)

    # Fetch Forex rate
    rate = client.get_forex_rate("USD", "EUR")
    print(rate)

    # Fetch cryptocurrency data
    df_crypto = client.get_crypto_data("BTC-USD", start="2023-01-01", end="2023-06-30")
    print(df_crypto)
"""

import yfinance as yf
from forex_python.converter import CurrencyRates
import requests
import pandas as pd
from typing import Optional


class DataAPIClient:
    """
    A client for interacting with various financial and data APIs.
    """

    def __init__(self):
        """
        Initialize the DataAPIClient.
        """
        self.currency_converter = CurrencyRates()

    def get_stock_data(self, ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
        """
        Fetch historical stock data from Yahoo Finance.

        :param ticker: The stock ticker symbol (e.g., "AAPL" for Apple).
        :param start: The start date for the data (YYYY-MM-DD).
        :param end: The end date for the data (YYYY-MM-DD).
        :param interval: The interval for the data (e.g., "1d", "1wk", "1mo").
        :return: A pandas DataFrame with the stock data.
        """
        try:
            df = yf.download(ticker, start=start, end=end, interval=interval)
            df.dropna(inplace=True)
            return df
        except Exception as e:
            print(f"An error occurred while fetching stock data: {e}")
            return pd.DataFrame()

    def get_forex_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate between two currencies.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            rate = self.currency_converter.get_rate(base_currency, target_currency)
            return rate
        except Exception as e:
            print(f"An error occurred while fetching forex rates: {e}")
            return None

    def get_crypto_data(self, ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
        """
        Fetch historical cryptocurrency data from Yahoo Finance.

        :param ticker: The cryptocurrency ticker symbol (e.g., "BTC-USD" for Bitcoin).
        :param start: The start date for the data (YYYY-MM-DD).
        :param end: The end date for the data (YYYY-MM-DD).
        :param interval: The interval for the data (e.g., "1d", "1wk", "1mo").
        :return: A pandas DataFrame with the cryptocurrency data.
        """
        try:
            df = yf.download(ticker, start=start, end=end, interval=interval)
            df.dropna(inplace=True)
            return df
        except Exception as e:
            print(f"An error occurred while fetching cryptocurrency data: {e}")
            return pd.DataFrame()

    def get_html_data(self, url: str) -> Optional[str]:
        """
        Fetch raw HTML data from a given URL.

        :param url: The URL to fetch HTML data from.
        :return: The raw HTML content as a string.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching HTML data: {e}")
            return None


# Example usage
if __name__ == "__main__":
    client = DataAPIClient()

    # Example: Fetch Apple stock data
    stock_data = client.get_stock_data("AAPL", start="2023-01-01", end="2023-06-30")
    print(stock_data)

    # Example: Fetch USD to EUR exchange rate
    forex_rate = client.get_forex_rate("USD", "EUR")
    print(forex_rate)

    # Example: Fetch Bitcoin data
    crypto_data = client.get_crypto_data("BTC-USD", start="2023-01-01", end="2023-06-30")
    print(crypto_data)

    # Example: Fetch HTML data from a website
    html_content = client.get_html_data("https://example.com")
    print(html_content[:500])  # Print the first 500 characters of the HTML content
