
import streamlit as st
"""
st.title("Home")
st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
if st.button('Say hello'):
     st.write('Why hello there')
 else:
     st.write('Goodbye')

st.image("footer.png",width=900)   
"""
import streamlit as st
import pickle as pkle
import os.path

pages = ['Home','About','Page3']

if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(pages):
        next_clicked = 0 
else:
    next_clicked = 0 

if next:
    next_clicked = next_clicked+1
    if next_clicked == len(pages):
        next_clicked = 0 

choice = st.sidebar.radio("Pages",('Home','about', 'Page3'), index=next_clicked)
pkle.dump(pages.index(choice), open('next.p', 'wb'))

if choice == 'Page1':
    st.title('Page 1')
elif choice == 'Page2':
    st.title('Page 2')
elif choice == 'Page3':
    st.title('Page 3')

next = st.button('Go to next page')

