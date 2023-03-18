import streamlit as st
import pandas as pd

st.title('Kickstarter Projects Analysis')

@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! Data is now cached and shouldn't take much to reload ^_^")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Projects by category')
category_data = data['Category'].value_counts()
st.bar_chart(category_data)

st.subheader('Projects by state')
state_data = data['State'].value_counts()
st.bar_chart(state_data)