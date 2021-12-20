import streamlit as st
st.title("Home")
st.image("Home1.png",width=900)  

img1="Home1.png"
img1="Home2.png"
img1="Home3.png"
start_color, end_color = st.select_slider(
     'Gallary',
     Option=['','',''],
     value=st.image("Home2.png",width=900))
st.write(img1)         
img4=st.image("Home4.png",width=900)      
         
         
        
