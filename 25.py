import streamlit as st
st.title("Skin Cancer Classfication ")

ID = st.text_input("ID")
name = st.text_input("Name")
age = st.text_input(" Age")
option = st.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
file = st.file_uploader("Upload Cancer photo")
st.write
# date = st.date_input("Pick a date")
page_bg_img = '''
<style>
body {
background-image: url("https://prodigits.co.uk/thumbs/wallpapers/p2ls/patterns/49/6385a8d612611973.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
if st.button('Say hello'):
     st.write('Why hello there')
        
