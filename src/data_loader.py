import pandas as pd


def load_data():

   df = pd.read_csv("data/raw/retail_store_inventory (1).csv")

   return df