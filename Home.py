import streamlit as st
st.title("Home")
st.image("Home1.png",width=900)  

img1="Home1.png"
img1="Home2.png"
img1="Home3.png"
start_color, end_color = st.select_slider(
     'Gallary',
     value=(img1,img2,img3))
st.write(img1)         
img4=st.image("Home4.png",width=900)      
         
         
        
