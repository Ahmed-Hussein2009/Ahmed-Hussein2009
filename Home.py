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
  body {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    --line-offset: calc((10vh + 8px) / 2);
}

.container {
    width: 70vw;
    height: 100vh;
    display: grid;
    grid-template-rows: 5fr 1fr;
    background: #021919;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
    justify-content: center;
    display: flex;
}

.tab {
    width: calc(10vh +8px);
    height: calc(10vh + 8px);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    clip-path: polygon(0% 50%, 15% 0%, 85% 0%, 100% 50%, 85% 100%, 15% 100%);
    shape-outside: polygon(0% 50%, 15% 0%, 85% 0%, 100% 50%, 85% 100%, 15% 100%);
    z-index: 0;
    transition: width 0.5s;
}

.tab img {
    width: 10vh;
    height: 10vh;
    z-index: 10;
    cursor: pointer;
    clip-path: polygon(0% 50%, 15% 0%, 85% 0%, 100% 50%, 85% 100%, 15% 100%);
    shape-outside: polygon(0% 50%, 15% 0%, 85% 0%, 100% 50%, 85% 100%, 15% 100%);
    transition: width 0.5s;
}

[type=radio] {
    display: none;   
}

.preview-list {
    background: linear-gradient(
        #021919,
        #021919 var(--line-offset),
        #efefef var(--line-offset)
    );
}

.tab {
    background: linear-gradient(
        #efefef,
        #efefef var(--line-offset),
        #021919 var(--line-offset)
    );
}

[type=radio]:checked ~ label ~ .content{
    text-align: center;
    z-index: 8;
}


[type=radio]:checked ~ label .tab{
    width: 0;
}

.content {
    position: absolute;
    background: #021919;
    top: 1vh;
    left: 0;
    width: 50vw;
    height: 80vh;
    overflow: hidden;
    display: flex;
    align-items: center;
}

.content img {
    height: 10;
    width: 10;  
}
 </style>
  <div class="container">
        <div class="full-view"></div>
        <div class="preview-list">
            <ul>
                <li>
                    <input type="radio" id="tab-1" name="gallery-group">
                    <label for="tab-1">
                        <div class="tab">
                            <img
                                src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home1.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
                        </div>
                    </label>
                    <div class="content">
                        <img
                            src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home1.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-2" name="gallery-group">
                    <label for="tab-2">
                        <div class="tab">
                            <img
                                src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home2.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
                        </div>
                    </label>
                    <div class="content">
                        <img
                            src="https:https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home2.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
                    </div>
                </li>
                <li>
                    <input type="radio" id="tab-3" name="gallery-group">
                    <label for="tab-3">
                        <div class="tab">
                            <img
                                src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home3.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
                        </div>
                    </label>
                    <div class="content">
                        <img width="1800" height="600"
                            src="https://raw.githubusercontent.com/Ahmed-Hussein2009/Ahmed-Hussein2009/main/Home3.png?auto=compress&cs=tinysrgb&dpr=2&h=750&w=500" />
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
