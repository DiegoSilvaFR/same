import psycopg2 as pg
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
import os

@st.cache_data
def raw_data_to_df(query: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns the result as a pandas DataFrame.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        df (pandas.DataFrame): DataFrame containing the query results.

    Raises:
        psycopg2.Error: If there is an error executing the query.
    """
    
    load_dotenv()

    conn = pg.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
    


    
    try:

        df = pd.read_sql(query, con=conn) 
        return df
       
        
 

    except pg.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        
    finally:
       
        conn.close()