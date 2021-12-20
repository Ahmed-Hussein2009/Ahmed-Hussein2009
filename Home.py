import streamlit as st

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
  <a class="navbar-brand" href="#r" target="_blank">Skin Cancer Classfication </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="Flase" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div style="float:left;" class="collapse navbar-collapse" id="navbarNav" >
    <ul class="navbar-nav">style="float:left;width:50%"
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">&nbsp&nbsp&nbsp&nbsp&nbsp <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="https://share.streamlit.io/ahmed-hussein2009/ahmed-hussein2009/main/25.py">Tools <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Solution <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="https://share.streamlit.io/ahmed-hussein2009/ahmed-hussein2009/main/about.py">About <span class="sr-only">(current)</span></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)






st.markdown("""

<a href="#img1">
  <img class="thumb" src="Home1.png">
</a>
<!-- lightbox container hidden with CSS -->
<div class="lightbox" id="img1">
  <a href="#img3" class="light-btn btn-prev">prev</a>
    <a href="#_" class="btn-close">X</a>
    <img src="Home1.png">
  <a href="#img2" class="light-btn btn-next">next</a>
</div>

<a href="#img2">
<img class="thumb" src="Home2.png">
</a>
<!-- lightbox container hidden with CSS -->
<div class="lightbox" id="img2">
  <a href="#img1" class="light-btn btn-prev">prev</a>
    <a href="#_" class="btn-close">X</a>
    <img src="Home2.png">
  <a href="#img3" class="light-btn btn-next">next</a>
</div>

<a href="#img3">
<img class="thumb" src="Home3.png">
</a>
<!-- lightbox container hidden with CSS -->
<div class="lightbox" id="img3">
  <a href="#img2" class="light-btn btn-prev">prev</a>
    <a href="#_" class="btn-close">X</a>
    <img src="Home3.png">
  <a href="#img1" class="light-btn btn-next">next</a>
</div>""", unsafe_allow_html=True)

st.title("Home")

st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
