import random
import time

import pandas as pd
import streamlit as st

st.title("Clinic Waiting Time Estimator")

with st.form("clinic_form"):
    num_nurses = st.slider("Number of nurses", min_value=1, max_value=10, value=2)
    num_runs = st.slider("Number of runs", min_value=1, max_value=20, value=5)
    run = st.form_submit_button("Run model")

if run:
    with st.spinner("Running model..."):
        results = []
        for i in range(num_runs):
            time.sleep(0.5)
            mean_wait = max(0, random.gauss(30 / num_nurses, 2))
            results.append({"Run": i + 1, "Mean wait (mins)": round(mean_wait, 1)})
    st.dataframe(pd.DataFrame(results).set_index("Run"))
