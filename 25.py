import streamlit as st
st.title("Skin Cancer Classfication ")
st.write("ID")
your_name = st.text_input("Enter your name")
col_one.header("Column 1")
col_two.header("Column 2")
file = st.file_uploader("Upload Cancer photo")

date = st.date_input("Pick a date")
number = st.slider("Pick a number", 0, 100)
