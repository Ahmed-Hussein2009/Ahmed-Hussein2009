import streamlit as st
st.title("Home")
img1=st.image("Home1.png",width=900)  
start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
st.write(img1)         
img4=st.image("Home4.png",width=900)      
         
         
        
