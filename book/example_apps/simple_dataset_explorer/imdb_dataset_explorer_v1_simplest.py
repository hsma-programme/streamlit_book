import pandas as pd
import plotly.express as px
import streamlit as st

st.title("IMDB Dataset Explorer")

# Import data
url = (
    "https://github.com/hsma-programme/streamlit_book/blob/main/book/datasets/imdb_top_1000.csv"
)
data = pd.read_csv(url)

# Display data
st.dataframe(data)

st.plotly_chart(px.histogram(data, x="Released_Year"))
