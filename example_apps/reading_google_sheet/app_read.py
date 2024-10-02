import streamlit as st
from streamlit_gsheets import GSheetsConnection # this doesn't exist in the hsma_webdev environment
# would need to be installed with
# !pip install st-gsheets-connection

# Confirm access to the secrets file
st.write("The secret word is:", st.secrets["test_secret"])

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Passing in 'Sheet1' returns a '400 resource not found error'
# Passing in the index of the sheet as an integer works!
df = conn.read(worksheet=0)

st.dataframe(df)
