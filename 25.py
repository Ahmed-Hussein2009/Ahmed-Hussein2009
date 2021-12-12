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


components.html("""<img src="https://static.semrush.com/blog/uploads/media/43/b0/43b0b9a04c8a433a0c52360c9cc9aaf2/seo-guide-to-yoast-for-wordpress.svg" alt="yoast seo" height="288" width="388"/>""")

        
