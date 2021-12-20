#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp()
def my_home():
 hy.info('Hello from app1')

@app.addapp()
def app2():
 hy.info('Hello from app 2')


#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()
app = HydraApp(title='Secure Hydralit Data Explorer',favicon="?",hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True)

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
