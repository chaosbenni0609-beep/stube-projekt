import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Create connection
def test_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="user",  # Replace with your password
            database="datab"  # Replace with your database name
        )
        if connection.is_connected():
            print("Connection successful!")
            return connection
    except Error as e:
        print(f"Error: {e}")
 
#test_connection()
#fetch records
def fetchData():
    conn = test_connection()
    if conn:
        try:
            query = "SELECT * FROM tab"
            donors = pd.read_sql(query, conn)
            return donors
        except Error as e:
            st.error(f"Error while fetching donor data: {str(e)}")
        finally:
            conn.close()
    else:
        return pd.DataFrame()  # Return an empty DataFrame if connection fails
    
st.title("Blood donation camp")
st.subheader("Registered users")
df=fetchData()
st.dataframe(df)
st.subheader("Registration - Form")