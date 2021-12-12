import streamlit as st
import streamlit.components.v1 as components
st.title("Skin Cancer Classfication ")

ID = st.text_input("ID")
name = st.text_input("Name")
age = st.text_input(" Age")
option = st.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
file = st.file_uploader("Upload Cancer photo")
st.write(file)
# date = st.date_input("Pick a date")


components.html("""<div style="background-image: url('img_girl.jpg');">""")

        
