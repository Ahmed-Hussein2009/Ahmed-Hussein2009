
import streamlit as st
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
import streamlit as st
import pandas as pd
import numpy as np

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class
class MySampleApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------
        st.title('Uber pickups in NYC')

        DATE_COLUMN = 'date/time'
        DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                    'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

        @st.cache
        def load_data(nrows):
            data = pd.read_csv(DATA_URL, nrows=nrows)
            lowercase = lambda x: str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
            return data

        data_load_state = st.text('Loading data...')
        data = load_data(10000)
        data_load_state.text("Done! (using st.cache)")

        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(data)

        st.subheader('Number of pickups by hour')
        hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.bar_chart(hist_values)

        # Some number in the range 0-23
        hour_to_filter = st.slider('hour', 0, 23, 17)
        filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

        st.subheader('Map of all pickups at %s:00' % hour_to_filter)
        st.map(filtered_data)
        #-------------------existing untouched code------------------------------------------
