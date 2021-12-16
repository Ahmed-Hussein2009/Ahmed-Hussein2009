import streamlit as st
import streamlit.components.v1 as components
st.title("Skin Cancer Classfication ")

form = st.form(key='my_form')
         
ID = form.text_input("ID")
name = form.text_input("Name")
age = form.number_input(" Age",step=5)
option = form.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
form.image("1.png", caption='skin cancser photo',width=650)
file = form.file_uploader("Upload Cancer photo")
# form.image("1.png", caption='Sunrise by the mountains')
# form.text_input(label='Enter some text')

submit_button = form.form_submit_button(label='Submit')

         
 
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
# st.write(file)
# # date = st.date_input("Pick a date")
# components.html("""
# <style>
# body {
#   background-image: url('img_girl.jpg');
# }
# </style>""")
# components.html("""<div ">asd</div>""")
# color = st.color_picker('Pick A Color', '#00f900')
# st.write('The current color is', color)

        
