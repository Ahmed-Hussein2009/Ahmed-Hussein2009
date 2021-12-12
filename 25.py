import streamlit as st
st.title("Skin Cancer Classfication ")

name = st.text_input("ID")
name = st.text_input("Name")
age = st.text_input(" Age")
st.write("Gender")
option = st.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
file = st.file_uploader("Upload Cancer photo")

# date = st.date_input("Pick a date")
if st.button('Say hello'):
     st.write('Why hello there')

