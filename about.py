import streamlit as st
import streamlit.components.v1 as components
st.title("About us")
st.image("about.png")
st.image("footer.png",width=700)   
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('1.png')
#width=650   
         
         
         
         
         
        
