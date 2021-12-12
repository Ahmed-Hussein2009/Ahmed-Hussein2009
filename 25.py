import streamlit as st
st.title("Skin Cancer Classfication ")
file = st.file_uploader("Pick a file")

date = st.date_input("Pick a date")
number = st.slider("Pick a number", 0, 100)
