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

<h1><a href="https://benschwarz.github.io/gallery-css/">Pure CSS-Gallery</a> by Ben Schwarz</h1>
<div class="gallery autoplay items-3">
	<div id="item-1" class="control-operator"></div>
	<div id="item-2" class="control-operator"></div>
	<div id="item-3" class="control-operator"></div>

	<figure class="item">
		<img src="http://lorempixel.com/800/400" class="flexible" alt="" />
	</figure>

	<figure class="item">
		<img src="http://placekitten.com/800/400" class="flexible" alt="" />
	</figure>

	<figure class="item">
		<img src="http://unsplash.it/800/400" class="flexible" alt="" />
	</figure>

	<figure class="item">
		<img src="http://placeimg.com/800/400" class="flexible" alt="" />
	</figure>

	<figure class="item">
		<img src="http://placebeer.com/800/400" class="flexible" alt="" />
	</figure>

	<div class="controls">
		<a href="#item-1" class="control-button">•</a>
		<a href="#item-2" class="control-button">•</a>
		<a href="#item-3" class="control-button">•</a>
		<a href="#item-4" class="control-button">•</a>
		<a href="#item-5" class="control-button">•</a>
	</div>
</div>""", unsafe_allow_html=True)

st.title("Home")

st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
