import streamlit as st
st.title("Home")
st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.button("Click me for no reason")
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

st.image("footer.png",width=900)   
