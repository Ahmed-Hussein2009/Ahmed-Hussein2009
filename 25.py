import streamlit as st
st.title("Skin Cancer Classfication ")
st.write("ID")
name = st.text_input("Enter your name")
st.write("Name")
name = st.text_input("Enter your name")
st.write("age")
name = st.text_input("Enter your name")
option = st.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
file = st.file_uploader("Upload Cancer photo")

# date = st.date_input("Pick a date")
if st.button('Say hello'):
     st.write('Why hello there')

