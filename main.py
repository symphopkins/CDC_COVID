import requests
import pandas as pd
import io
import psycopg2
from sqlalchemy import create_engine

# EXTRACT
def retrieve_cdc_data(limit=1000):

  """
  Extracts data from the CDC API.

  Args:
      limit (int): The number of records returned.

  Returns:
      pandas.DataFrame: The extracted data as a DataFrame.
  """

  url = "https://data.cdc.gov/resource/jr58-6ysp.csv"
  response = requests.get(url, params={'$limit': limit})
  response_text = response.text
  csv_file = io.StringIO(response_text)
  df = pd.read_csv(csv_file)
  return df

df = retrieve_cdc_data(limit=2000000)
print(df.head())

# TRANSFORM
def convert_to_date(df, columns):
  """
  Convert specified columns in a DataFrame to date format.

  Parameters:
      df (DataFrame): The DataFrame to be modified.
      columns (list of str): List of column names to convert to date format.

  Returns:
      DataFrame: The DataFrame with specified columns converted to date format.
  """
  for column in columns:
      df[column] = pd.to_datetime(df[column]).dt.date
  return df

df = convert_to_date(df, ['week_ending','creation_date'])
print(df.head())


def map_to_hhs_regions(df):
  """
  Map values in a DataFrame column to corresponding HHS regions using a predefined mapping.

  Parameters:
      df (DataFrame): The DataFrame containing the column to be mapped.

  Returns:
      DataFrame: The DataFrame with the column mapped to HHS regions.
  """
  hhs_regions = {
      "USA": "USA",
      "1": "Boston",
      "2": "New York",
      "3": "Philadelphia",
      "4": "Atlanta",
      "5": "Chicago",
      "6": "Dallas",
      "7": "Kansas City",
      "8": "Denver",
      "9": "San Francisco",
      "10": "Seattle"
  }
  df['hhs_regions'] = df['usa_or_hhsregion'].map(hhs_regions)
  return df

df = map_to_hhs_regions(df)
print(df.head())

# LOAD
def load_data_to_postgresql(df, table_name, conn_string):
    """
    Load data from a DataFrame into a PostgreSQL table.

    Parameters:
        df (DataFrame): The DataFrame containing the data to be loaded.
        table_name (str): The name of the PostgreSQL table to load the data into.
        conn_string (str): The connection string for connecting to the PostgreSQL database.

    Returns:
        None
    """
    try:
        engine = create_engine(conn_string)
        
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print("Data loaded successfully.")

    except Exception as e:
        print("Error:", e)

your_connection_string = "str"
load_data_to_postgresql(df, 'variant_proportions', your_connection_string)