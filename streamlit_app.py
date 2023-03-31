# streamlit_app.py

import streamlit as st
import pandas as pd
import snowflake.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from TRIPS limit 10;")
st.write("hello")
#st.write(rows)
columns =['TRIPDURATION', 'STARTTIME', "TRIPDURATION","STARTTIME",	"STOPTIME"	,"START_STATION_ID"	,"START_STATION_NAME"	,"START_STATION_LATITUDE"	,"START_STATION_LONGITUDE"	,"END_STATION_ID"	,"END_STATION_NAME"	,"END_STATION_LATITUDE"	,"END_STATION_LONGITUDE","BIKEID"	,"MEMBERSHIP_TYPE"	,"USERTYPE"	,"BIRTH_YEAR"	,"GENDER"]
df = pd.DataFrame(rows, columns=columns)
st.write(df)