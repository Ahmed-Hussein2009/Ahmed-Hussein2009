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


components.html("""<div style="background-image: url('https://res.cloudinary.com/practicaldev/image/fetch/s--UIhCZbfu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/wobsu31ey0fr1bn91rq2.gif');">""")

        
