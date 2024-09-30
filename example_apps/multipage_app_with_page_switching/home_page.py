import streamlit as st

st.title("Clinic Simulation App")

st.write("Welcome to the clinic simulation app!")

if st.button("Click here to head to the simulation page"):
    st.switch_page("des_page.py")
