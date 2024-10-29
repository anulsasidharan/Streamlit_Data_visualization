import streamlit as st
import pandas as pd
import plotly_express as px
import xlrd
from docutils.nodes import label
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


# Would you like display the data
display_data = st.sidebar.checkbox(label="Would you lke to view the uploaded datasets")

# print(uploaded_file)


global df
#  account for the cases where uploaded file is not none.
if uploaded_file is not None:
    try:
        # Read the csv file
        df = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

    if display_data:
        # Write teh data into the main page
        st.write(df)

    # Extract numeric columns as list
    numeric_cols = list(df.select_dtypes(['float', 'int']).columns)

    # Extract the non-numeric columns
    non_numeric_columns = list(df.select_dtypes(['object']).columns)

    # Append None to non_numeric list
    non_numeric_columns.append('None')

    # Write data into main page
    # st.write(numeric_cols)
    # st.write(non_numeric_columns)

# Add select widget
chart_select = st.sidebar.selectbox(
    label="Select the visualization type",
    options=['Scatterplot', 'Lineplot', 'Histogram']
)
print(chart_select)

try:
    ## Scatter Plot
    if chart_select == "Scatterplot":
        st.sidebar.subheader("Setting for Scatterplot")
        x_value = st.sidebar.selectbox(label="X axis",
                                       options=numeric_cols
                                       )
        y_value = st.sidebar.selectbox(label="Y axis",
                                       options=numeric_cols
                                       )
        specify_color = st.sidebar.checkbox(label="Would you like to specify the color?")
        if specify_color:
            color_value = st.sidebar.selectbox(label="Color",
                                           options=non_numeric_columns
                                           )

            plot = px.scatter(data_frame=df, x=x_value,
                          y=y_value, color=color_value
                          )
        else:
            plot = px.scatter(data_frame=df, x=x_value,
                              y=y_value
                              )
        #Display chart in streamlit
        st.plotly_chart(plot)

    # Histogram
    if chart_select == "Histogram":
        st.sidebar.subheader("Setting for Histogram")
        x = st.sidebar.selectbox(label="Feature",
                                       options=numeric_cols
                                       )
        bin_size = st.sidebar.slider(label="number of bins",
                                     min_value=10,
                                     max_value=100,
                                     value=50)


        plot = px.histogram(data_frame=df, x=x,
                      nbins=bin_size
                      )
        #Display chart in streamlit
        st.plotly_chart(plot)

    ## Line Plot
    if chart_select == "Lineplot":
        st.sidebar.subheader("Setting for Lineplot")
        x_value = st.sidebar.selectbox(label="X axis",
                                       options=numeric_cols
                                       )
        y_value = st.sidebar.selectbox(label="Y axis",
                                       options=numeric_cols
                                       )
        plot = px.line(data_frame=df, x=x_value,
                       y=y_value
                       )
        # Display chart in streamlit
        st.plotly_chart(plot)


except Exception as e:
    print(e)
