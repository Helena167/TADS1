import yfinance as yf 
import pandas as pd

def download_data(ticker:str) -> pd.DataFrame:
    """_summary_

    Args:
        ticker (str): the ticker of financial asset.

    Returns:
        pd.DataFrame: A dateframe retired from yahoo.
    """
    data = yf.download(ticker)

    return data