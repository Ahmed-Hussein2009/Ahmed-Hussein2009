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

 <div class="container">
        <div class="full-view"></div>
        <div class="preview-list">
            <ul>
                <li>
                    <input type="radio" id="tab-1" name="gallery-group">
                    <label for="tab-1">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/1559117/pexels-photo-1559117.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                        <img
                            src="https://images.pexels.com/photos/1559117/pexels-photo-1559117.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-2" name="gallery-group">
                    <label for="tab-2">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/688660/pexels-photo-688660.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                        <img
                            src="https://images.pexels.com/photos/688660/pexels-photo-688660.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-3" name="gallery-group">
                    <label for="tab-3">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/730256/pexels-photo-730256.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                        <img
                            src="https://images.pexels.com/photos/730256/pexels-photo-730256.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-4" name="gallery-group" checked>
                    <label for="tab-4">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/22427/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                        <img src="https://images.pexels.com/photos/22427/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-5" name="gallery-group">
                    <label for="tab-5">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/789380/pexels-photo-789380.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                            <img src="https://images.pexels.com/photos/789380/pexels-photo-789380.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                </li>
                <li>
                    <input type="radio" id="tab-6" name="gallery-group">
                    <label for="tab-6">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/355411/pexels-photo-355411.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" />
                        </div>
                    </label>
                    <div class="content">
                            <img src="https://images.pexels.com/photos/355411/pexels-photo-355411.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" />
                        </div>
                </li>
                <li>
                    <input type="radio" id="tab-7" name="gallery-group">
                    <label for="tab-7">
                        <div class="tab">
                            <img
                                src="https://images.pexels.com/photos/1424246/pexels-photo-1424246.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                    </label>
                    <div class="content">
                            <img src="https://images.pexels.com/photos/1424246/pexels-photo-1424246.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" />
                        </div>
                </li>
            </ul>
        </div>
    </div>

""", unsafe_allow_html=True)

st.title("Home")

st.image("Home1.png",width=900)  
st.image("Home2.png",width=900)  
st.image("Home3.png",width=900)  
img4=st.image("Home4.png",width=900)  
st.image("footer.png",width=900)   
