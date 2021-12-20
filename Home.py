import streamlit as st
st.title("Home")

start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
st.write('You selected wavelengths between', start_color,)         
st.image("footer.png",width=1200)      
         
         
        
