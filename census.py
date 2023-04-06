import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run netflix.py 
st.set_page_config(page_title="INDIA CENSUS  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6111-E Jeji Anil", "21A21A6158-Tusha Rahul B ", "21A21A6137-M S R Chandrika","21A21A6166-K Shyam chand","21A21A6101-A Leena","21A21A6140-N Upendra","21A21A6157-T Sumanth Raju","22A25A6105(L5)-T Naveen Babu"]
st.title("Exploratory Data Analysis on India Census Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a India Census Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("India Census Data Analysis")
    if st.checkbox("How will you hide the indexes of the dataframe?"):
        st.write(data.style.hide_index())
    if st.checkbox("How can we set the caption / heading on the dataframe?"):
        st.write(data.style.set_caption('India Census 2011 Dataset'))
    if st.checkbox("Show the records related with the districts - New Delhi , Lucknow , Jaipur"):
        st.write(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])
    if st.checkbox("Calculate state-wise total number of popluation and population with different religions"):
        st.write(data.groupby('State_name').agg({'Population': 'sum', 'Hindus': 'sum', 'Muslims': 'sum', 'Christians': 'sum', 'Sikhs': 'sum', 'Buddhists': 'sum', 'Jains': 'sum'}).sort_values(by='Population', ascending=False))
    if st.checkbox("How many Male Workers were there in Maharashtra state ?"):
        st.write(data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum())
    if st.checkbox(" How to set a column as index of the dataframe ?"):
        st.write(data.set_index('District_code'))
    if st.checkbox("Add a Suffix to the column names"):
        st.write(data.add_suffix('_rightone'))
    if st.checkbox("Add a Prefix to the column names"):
        st.write(data.add_prefix('leftone_'))
        
