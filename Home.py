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
 html,
body {
  height: 100%;
  margin: 0px;
}

.slider-container {
  
  display: flex;
  align-items: left;
  justify-content: left;
  height: 140%;
  width: 180%;
}

.slider {
  width: 100%;
  max-width: 800px;
  height: 400px;
  margin: 50px;
  text-align: center;
  border-radius: 20px;
  overflow: hidden;
  position: relative;
}

.slides {
  display: flex;
  overflow-x: scroll;
  position: relative;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
}

.slide:nth-of-type(even) {
  background-color: rgb(250, 246, 212);
}

.slide {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  width: 100%;
  height: 400px;
  scroll-snap-align: center;
  margin-right: 0px;
  box-sizing: border-box;
  background: white;
  transform-origin: center center;
  transform: scale(1);
}

.slide__text {
  font-size: 40px;
  font-weight: bold;
  font-family: sans-serif;
}

.slide a {
  background: none;
  border: none;
}

a.slide__prev,
.slider::before {
  transform: rotate(135deg);
  -webkit-transform: rotate(135deg);
  left: 5%;
}

a.slide__next,
.slider::after {
  transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
  right: 5%;
}

.slider::before,
.slider::after,
.slide__prev,
.slide__next {
  position: absolute;
  top: 48%;
  width: 35px;
  height: 35px;
  border: solid black;
  border-width: 0 4px 4px 0;
  padding: 3px;
  box-sizing: border-box;
}

.slider::before,
.slider::after {
  content: "";
  z-index: 1;
  background: none;
  pointer-events: none;
}

.slider__nav {
  box-sizing: border-box;
  position: absolute;
  bottom: 5%;
  left: 50%;
  width: 200px;
  margin-left: -100px;
  text-align: center;
}

.slider__navlink {
  display: inline-block;
  height: 15px;
  width: 15px;
  border-radius: 50%;
  background-color: black;
  margin: 0 10px 0 10px;
}








.read-article{
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 999;
  color: #000;
  background: white;
  padding: 10px 20px;
  border-radius: 10px;
  font-family: arial;
  text-decoration: none;
  box-shadow: rgb(50 50 93 / 25%) 0 0 100px -20px, rgb(0 0 0 / 30%) 0 0 60px -15px;
}
.read-article:hover{
    background: #d5d5d5;
    box-shadow: rgb(50 50 93 / 25%) 0 0 100px -20px, rgb(0 0 0 / 30%) 0 0 60px 0px;
}
iframe[sandbox] .read-article{
  display: none;
}
</style>
 <div class="slider-container">
  <div class="slider">
    <div class="slides">
      <div id="slides__1" class="slide">
        <span class="slide__text"><img width="800" height="400" src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home1.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" /></span>
        <a class="slide__prev" href="#slides__3" title="Next"></a>
        <a class="slide__next" href="#slides__2" title="Next"></a>
      </div>
      <div id="slides__2" class="slide">
        <span class="slide__text"><img width="800" height="400" src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home2.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" /></span>
        <a class="slide__prev" href="#slides__1" title="Prev"></a>
        <a class="slide__next" href="#slides__3" title="Next"></a>
      </div>
      <div id="slides__3" class="slide">
        <span class="slide__text"><img width="800" height="400" src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home3.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" /></span>
        <a class="slide__prev" href="#slides__2" title="Prev"></a>
        <a class="slide__next" href="#slides__1" title="Prev"></a>
      </div>
    </div>
    <div class="slider__nav">
      <a class="slider__navlink" href="#slides__1"></a>
      <a class="slider__navlink" href="#slides__2"></a>
      <a class="slider__navlink" href="#slides__3"></a>
    </div>
  </div>
</div>


""", unsafe_allow_html=True)

st.title("Home")

# st.image("Home1.png",width=900)  
# st.image("Home2.png",width=900)  
# st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
