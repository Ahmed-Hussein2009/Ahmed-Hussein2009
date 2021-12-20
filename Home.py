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

.gallery .control-operator:target ~ .controls .control-button {
  color: #ccc;
  color: rgba(255, 255, 255, 0.4);
}

.gallery .control-button:first-of-type, 
.items-2 .control-operator:nth-of-type(1):target ~ .controls .control-button:nth-of-type(1), 
.items-2 .control-operator:nth-of-type(2):target ~ .controls .control-button:nth-of-type(2), 
.items-3 .control-operator:nth-of-type(1):target ~ .controls .control-button:nth-of-type(1), 
.items-3 .control-operator:nth-of-type(2):target ~ .controls .control-button:nth-of-type(2), 
.items-3 .control-operator:nth-of-type(3):target ~ .controls .control-button:nth-of-type(3), 
.items-4 .control-operator:nth-of-type(1):target ~ .controls .control-button:nth-of-type(1), 
.items-4 .control-operator:nth-of-type(2):target ~ .controls .control-button:nth-of-type(2), 
.items-4 .control-operator:nth-of-type(3):target ~ .controls .control-button:nth-of-type(3), 
.items-4 .control-operator:nth-of-type(4):target ~ .controls .control-button:nth-of-type(4), 
.items-5 .control-operator:nth-of-type(1):target ~ .controls .control-button:nth-of-type(1), 
.items-5 .control-operator:nth-of-type(2):target ~ .controls .control-button:nth-of-type(2), 
.items-5 .control-operator:nth-of-type(3):target ~ .controls .control-button:nth-of-type(3), 
.items-5 .control-operator:nth-of-type(4):target ~ .controls .control-button:nth-of-type(4), 
.items-5 .control-operator:nth-of-type(5):target ~ .controls .control-button:nth-of-type(5) {
  color: white;
  color: rgba(255, 255, 255, 0.8);
}

.gallery .item:first-of-type {
  position: static;
  opacity: 1;
}
.gallery .item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity .5s;
}
.gallery .control-operator {
  display: none;
}
.gallery .control-operator:target ~ .item {
  pointer-events: none;
  opacity: 0;
  animation: none;
}
.gallery .control-operator:target ~ .controls .control-button {
  animation: none;
}

@keyframes controlAnimation-2 {
  0% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }

  14.3%,
  50% {
    color: white;
    color: rgba(255, 255, 255, 0.8);
  }

  64.3%,
  100% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }
}

@keyframes galleryAnimation-2 {
  0% {
    opacity: 0;
  }

  14.3%,
  50% {
    opacity: 1;
  }

  64.3%,
  100% {
    opacity: 0;
  }
}

.items-2.autoplay .control-button {
  animation: controlAnimation-2 14s infinite;
}
.items-2.autoplay .item {
  animation: galleryAnimation-2 14s infinite;
}
.items-2 .control-operator:nth-of-type(1):target ~ .item:nth-of-type(1) {
  pointer-events: auto;
  opacity: 1;
}
.items-2 .control-button:nth-of-type(1),
.items-2 .item:nth-of-type(1) {
  animation-delay: -2s;
}
.items-2 .control-operator:nth-of-type(2):target ~ .item:nth-of-type(2) {
  pointer-events: auto;
  opacity: 1;
}
.items-2 .control-button:nth-of-type(2),
.items-2 .item:nth-of-type(2) {
  animation-delay: 5s;
}

@keyframes controlAnimation-3 {
  0% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }

  9.5%,
  33.3% {
    color: white;
    color: rgba(255, 255, 255, 0.8);
  }

  42.9%,
  100% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }
}

@keyframes galleryAnimation-3 {
  0% {
    opacity: 0;
  }

  9.5%,
  33.3% {
    opacity: 1;
  }

  42.9%,
  100% {
    opacity: 0;
  }
}

.items-3.autoplay .control-button {
  animation: controlAnimation-3 21s infinite;
}
.items-3.autoplay .item {
  animation: galleryAnimation-3 21s infinite;
}
.items-3 .control-operator:nth-of-type(1):target ~ .item:nth-of-type(1) {
  pointer-events: auto;
  opacity: 1;
}
.items-3 .control-button:nth-of-type(1),
.items-3 .item:nth-of-type(1) {
  animation-delay: -2s;
}
.items-3 .control-operator:nth-of-type(2):target ~ .item:nth-of-type(2) {
  pointer-events: auto;
  opacity: 1;
}
.items-3 .control-button:nth-of-type(2),
.items-3 .item:nth-of-type(2) {
  animation-delay: 5s;
}
.items-3 .control-operator:nth-of-type(3):target ~ .item:nth-of-type(3) {
  pointer-events: auto;
  opacity: 1;
}
.items-3 .control-button:nth-of-type(3),
.items-3 .item:nth-of-type(3) {
  animation-delay: 12s;
}

@keyframes controlAnimation-4 {
  0% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }

  7.1%,
  25% {
    color: white;
    color: rgba(255, 255, 255, 0.8);
  }

  32.1%,
  100% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }
}

@keyframes galleryAnimation-4 {
  0% {
    opacity: 0;
  }

  7.1%,
  25% {
    opacity: 1;
  }

  32.1%,
  100% {
    opacity: 0;
  }
}

.items-4.autoplay .control-button {
  animation: controlAnimation-4 28s infinite;
}
.items-4.autoplay .item {
  animation: galleryAnimation-4 28s infinite;
}
.items-4 .control-operator:nth-of-type(1):target ~ .item:nth-of-type(1) {
  pointer-events: auto;
  opacity: 1;
}
.items-4 .control-button:nth-of-type(1),
.items-4 .item:nth-of-type(1) {
  animation-delay: -2s;
}
.items-4 .control-operator:nth-of-type(2):target ~ .item:nth-of-type(2) {
  pointer-events: auto;
  opacity: 1;
}
.items-4 .control-button:nth-of-type(2),
.items-4 .item:nth-of-type(2) {
  animation-delay: 5s;
}
.items-4 .control-operator:nth-of-type(3):target ~ .item:nth-of-type(3) {
  pointer-events: auto;
  opacity: 1;
}
.items-4 .control-button:nth-of-type(3),
.items-4 .item:nth-of-type(3) {
  animation-delay: 12s;
}
.items-4 .control-operator:nth-of-type(4):target ~ .item:nth-of-type(4) {
  pointer-events: auto;
  opacity: 1;
}
.items-4 .control-button:nth-of-type(4),
.items-4 .item:nth-of-type(4) {
  animation-delay: 19s;
}

@keyframes controlAnimation-5 {
  0% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }

  5.7%,
  20% {
    color: white;
    color: rgba(255, 255, 255, 0.8);
  }

  25.7%,
  100% {
    color: #ccc;
    color: rgba(255, 255, 255, 0.4);
  }
}

@keyframes galleryAnimation-5 {
  0% {
    opacity: 0;
  }

  5.7%,
  20% {
    opacity: 1;
  }

  25.7%,
  100% {
    opacity: 0;
  }
}

.items-5.autoplay .control-button {
  animation: controlAnimation-5 35s infinite;
}
.items-5.autoplay .item {
  animation: galleryAnimation-5 35s infinite;
}
.items-5 .control-operator:nth-of-type(1):target ~ .item:nth-of-type(1) {
  pointer-events: auto;
  opacity: 1;
}
.items-5 .control-button:nth-of-type(1),
.items-5 .item:nth-of-type(1) {
  animation-delay: -2s;
}
.items-5 .control-operator:nth-of-type(2):target ~ .item:nth-of-type(2) {
  pointer-events: auto;
  opacity: 1;
}
.items-5 .control-button:nth-of-type(2),
.items-5 .item:nth-of-type(2) {
  animation-delay: 5s;
}
.items-5 .control-operator:nth-of-type(3):target ~ .item:nth-of-type(3) {
  pointer-events: auto;
  opacity: 1;
}
.items-5 .control-button:nth-of-type(3),
.items-5 .item:nth-of-type(3) {
  animation-delay: 12s;
}
.items-5 .control-operator:nth-of-type(4):target ~ .item:nth-of-type(4) {
  pointer-events: auto;
  opacity: 1;
}
.items-5 .control-button:nth-of-type(4),
.items-5 .item:nth-of-type(4) {
  animation-delay: 19s;
}
.items-5 .control-operator:nth-of-type(5):target ~ .item:nth-of-type(5) {
  pointer-events: auto;
  opacity: 1;
}
.items-5 .control-button:nth-of-type(5),
.items-5 .item:nth-of-type(5) {
  animation-delay: 26s;
}

/* ------------------- */
.gallery .control-button {
  color: #ccc;
  color: rgba(255, 255, 255, 0.4);
}

.gallery .control-button:hover {
  color: white;
  color: rgba(255, 255, 255, 0.8);
}

/*
	Theme controls how everything looks in Gallery CSS.
*/
.gallery {
  position: relative;
}
.gallery .item {
  height: 400px;
  overflow: hidden;
  text-align: center;
  background: #4d87e2;
}
.gallery .controls {
  position: absolute;
  bottom: 0;
  width: 100%;
  text-align: center;
}
.gallery .control-button {
  display: inline-block;
  margin: 0 .02em;
  font-size: 3em;
  text-align: center;
  text-decoration: none;
  transition: color .1s;
}

/* ------------------- */
figure {
  margin: 1em 0;
}

.flexible {
  width: 100%;
  height: auto;
  max-width: 100%;
  display: block;
}

/* Nummern */
.gallery {
	counter-reset: numbers;
}
.item {
	counter-increment: numbers;
	position: relative;
}
.item:before {
	content: counter(numbers);
	background-color: #fff;
	font-size: 24px;
	border-radius: 50%;
	padding:  5px 10px;
	position: absolute;
	top: 10px;
	right: 10px;
}

</style>
<body>
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
	</div>
</body> """, unsafe_allow_html=True)

st.title("Home")

st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
