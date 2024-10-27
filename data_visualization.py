import streamlit as st
import pandas as pd
import plotly_express as px
from holoviews.operation import histogram

# Add a title
st.title("Data Visualization WebApp")

# Add a subtitle
st.sidebar.subheader("Visualization Settings")

# Add a file uploader
uploaded_file = st.sidebar.file_uploader(
    label="Upload your CSV or Excel file here; Size should be less than 200MB",
    type=['csv', 'xlsx']
)
# print(uploaded_file)

global df
#  account for the cases where uploaded file is not none.
if uploaded_file is not None:
    try:
        # Read the csv file
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df=pd.read_excel(uploaded_file)

    # Write teh data into the main page
    st.write(df)

    # Extract numeric columns as list
    numeric_cols = list(df.select_dtypes(['float', 'int']).columns)

    # Extract the non-numeric columns
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    # Write data into main page
    # st.write(numeric_cols)
    # st.write(non_numeric_columns)

