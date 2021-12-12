import streamlit as st
st.title("Skin Cancer Classfication ")
st.write("ID")
st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None)
file = st.file_uploader("Upload Cancer photo")

date = st.date_input("Pick a date")
number = st.slider("Pick a number", 0, 100)
