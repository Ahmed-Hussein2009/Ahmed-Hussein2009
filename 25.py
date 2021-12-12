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
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
if st.button('Say hello'):
     st.write('Why hello there')
        
