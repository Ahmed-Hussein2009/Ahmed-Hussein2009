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
<style>
.mySlides {display:none}
</style>



<div class="w3-content" style="max-width:800px">
  <img class="mySlides" src="Home1.png" style="width:100%">
  <img class="mySlides" src="Home2.png" style="width:100%">
  <img class="mySlides" src="Home3.png" style="width:100%">
</div>

<div class="w3-center">
  <div class="w3-section">
    <button class="w3-button w3-light-grey" onclick="plusDivs(-1)">❮ Prev</button>
    <button class="w3-button w3-light-grey" onclick="plusDivs(1)">Next ❯</button>
  </div>
  <button class="w3-button demo" onclick="currentDiv(1)">1</button> 
  <button class="w3-button demo" onclick="currentDiv(2)">2</button> 
  <button class="w3-button demo" onclick="currentDiv(3)">3</button> 
</div>

<script>
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-red", "");
  }
  x[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " w3-red";
}
</script>


""", unsafe_allow_html=True)




















st.markdown('''# **Skin Cancer Clssfication AI Program**''')

# Load market data from Binance API


st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

st.title("Home")

st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
