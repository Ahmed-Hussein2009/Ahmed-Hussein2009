import streamlit as st
import streamlit.components.v1 as components
st.title("About us")
st.image("about.png")
st.image("footer.png",width=700)   
def set_png_as_page_bg("1.png"):
    bin_str = get_base64_of_bin_file2(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
#width=650   
         
         
         
         
         
        
