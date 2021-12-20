import streamlit as st
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


st.title("Skin Cancer Classfication ")

form = st.form(key='my_form')
         
ID = form.text_input("ID")
name = form.text_input("Name")
age = form.number_input(" Age",step=5)
option = form.selectbox(
    "Select Gender",
    ["Male","Female" ]
)
form.image("2.png", caption='skin cancser photo',width=650)
file = form.file_uploader("Upload Cancer photo")
# form.image("1.png", caption='Sunrise by the mountains')
# form.text_input(label='Enter some text')

submit_button = form.form_submit_button(label='Submit')


st.image("footer.png",width=700)   
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
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

        
