import streamlit as st
st.title("Skin Cancer Classfication ")
st.write("ID")
st.text_input(label, value="", placeholder="asd")
file = st.file_uploader("Upload Cancer photo")

date = st.date_input("Pick a date")
number = st.slider("Pick a number", 0, 100)
