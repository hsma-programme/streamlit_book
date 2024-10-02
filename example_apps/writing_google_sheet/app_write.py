import streamlit as st
from streamlit_gsheets import GSheetsConnection # this doesn't exist in the hsma_webdev environment
import random
import numpy as np
import pandas as pd
from datetime import datetime
# would need to be installed with
# !pip install st-gsheets-connection

# Confirm access to the secrets file
st.write("The secret word is:", st.secrets["test_secret"])

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Passing in 'Sheet1' returns a '400 resource not found error'
# Passing in the index of the sheet as an integer works!
df = conn.read(worksheet=0, ttl=0)
st.dataframe(df.sort_values("Added", ascending=False))

if st.button("Update worksheet"):
    # Update the dataframe before overwriting in case any actions have been undertaken since the user first loaded the page
    df = conn.read(worksheet=0, ttl=0)

    # Generate an additional data field
    units = random.randint(100, 5000)
    unit_cost = np.round((random.random() + random.randint(1, 10)), 2)

    additional_row = [
        {'Item': "Additional HSMA Merchandise",
        "Category": random.choice(["Stickers", "Pets", "Clothing", "Mugs"]),
        "Units": units,
        "Unit Cost": unit_cost,
        "Total": units * unit_cost,
        "Added": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
    ]

    df_updated = pd.concat(
        [df,
        pd.DataFrame(additional_row)
        ]
    )

    df = conn.update(
        worksheet=0,
        data=df_updated,
    )
    st.cache_data.clear()
    st.rerun()

    # st.dataframe(df.sort_values("Added", ascending=False))
