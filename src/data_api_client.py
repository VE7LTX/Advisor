# src/data_api_client.py

"""
data_api_client.py - A collection of clients for interacting with various financial and data APIs.

This module provides a set of classes that encapsulate the functionality required to interact with various data sources
like Yahoo Finance, Forex rates, and others. Each class is dedicated to a specific API and provides methods for fetching
market data, exchange rates, and other relevant information.

Classes:
    - YahooFinanceAPI: Interacts with Yahoo Finance to fetch stock and cryptocurrency data.
    - ForexPythonAPI: Interacts with Forex-Python to fetch currency exchange rates.
    - OpenExchangeRatesAPI: Interacts with Open Exchange Rates to fetch exchange rates.
    - CurrencyLayerAPI: Interacts with CurrencyLayer to fetch exchange rates.
    - ExchangeRatesAPI: Interacts with ExchangeRatesAPI.io to fetch exchange rates.
    - AlphaVantageAPI: Interacts with Alpha Vantage to fetch exchange rates.
    - ExchangerateHostAPI: Interacts with Exchangerate.host to fetch exchange rates.

Key Features:
    - Encapsulated API interactions: Each API is represented by a separate class for modularity and clarity.
    - Error handling: Each method is wrapped in a try-except block to handle potential API errors gracefully.
    - Extensibility: New APIs can be easily integrated by adding new classes following the existing structure.

Usage Example:
    from data_api_client import YahooFinanceAPI, ForexPythonAPI, OpenExchangeRatesAPI

    # Initialize the API clients
    yahoo_client = YahooFinanceAPI()
    forex_client = ForexPythonAPI()
    open_exchange_client = OpenExchangeRatesAPI(api_key="YOUR_APP_ID")

    # Fetch stock data
    df = yahoo_client.get_stock_data("AAPL", start="2023-01-01", end="2023-06-30")
    print(df)

    # Fetch Forex rate
    rate = forex_client.get_forex_rate("USD", "EUR")
    print(rate)

    # Fetch exchange rate from Open Exchange Rates
    open_rate = open_exchange_client.get_rate("USD", "EUR")
    print(open_rate)

"""

import yfinance as yf
from forex_python.converter import CurrencyRates
import requests
import pandas as pd
from typing import Optional, Dict


class YahooFinanceAPI:
    """
    A client for interacting with Yahoo Finance API to fetch stock and cryptocurrency data.
    """

    @staticmethod
    def get_stock_data(ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
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

    @staticmethod
    def get_crypto_data(ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
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


class ForexPythonAPI:
    """
    A client for interacting with the Forex-Python API to fetch currency exchange rates.
    """

    def __init__(self):
        self.currency_converter = CurrencyRates()

    def get_forex_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate between two currencies using forex-python.

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


class OpenExchangeRatesAPI:
    """
    A client for interacting with the Open Exchange Rates API to fetch exchange rates.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate using the Open Exchange Rates API.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            url = f'https://openexchangerates.org/api/latest.json?app_id={self.api_key}&base={base_currency}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['rates'].get(target_currency)
        except Exception as e:
            print(f"An error occurred while fetching rates from Open Exchange Rates: {e}")
            return None


class CurrencyLayerAPI:
    """
    A client for interacting with the CurrencyLayer API to fetch exchange rates.
    """

    def __init__(self, access_key: str):
        self.access_key = access_key

    def get_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate using the CurrencyLayer API.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            url = f'http://api.currencylayer.com/live?access_key={self.access_key}&currencies={target_currency}&source={base_currency}&format=1'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['quotes'].get(f'{base_currency}{target_currency}')
        except Exception as e:
            print(f"An error occurred while fetching rates from CurrencyLayer: {e}")
            return None


class ExchangeRatesAPI:
    """
    A client for interacting with the ExchangeRatesAPI.io to fetch exchange rates.
    """

    @staticmethod
    def get_rate(base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate using the ExchangeRatesAPI.io.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            url = f'https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['rates'].get(target_currency)
        except Exception as e:
            print(f"An error occurred while fetching rates from ExchangeRatesAPI.io: {e}")
            return None


class AlphaVantageAPI:
    """
    A client for interacting with the Alpha Vantage API to fetch exchange rates.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate using the Alpha Vantage API.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={base_currency}&to_currency={target_currency}&apikey={self.api_key}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        except Exception as e:
            print(f"An error occurred while fetching rates from Alpha Vantage: {e}")
            return None


class ExchangerateHostAPI:
    """
    A client for interacting with the Exchangerate.host API to fetch exchange rates.
    """

    @staticmethod
    def get_rate(base_currency: str, target_currency: str) -> Optional[float]:
        """
        Retrieve the current exchange rate using the Exchangerate.host API.

        :param base_currency: The base currency code (e.g., "USD").
        :param target_currency: The target currency code (e.g., "EUR").
        :return: The exchange rate as a float.
        """
        try:
            url = f'https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['rates'].get(target_currency)
        except Exception as e:
            print(f"An error occurred while fetching rates from Exchangerate.host: {e}")
            return None
