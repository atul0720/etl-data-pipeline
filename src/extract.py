import pandas as pd
from config import RAW_DATA_PATH

def extract():
    return pd.read_csv(RAW_DATA_PATH)
