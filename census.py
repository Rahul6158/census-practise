import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px 
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run census.py 
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
    if st.checkbox("What are the columns present in the dataset"):
        st.write(data.columns)
    
    if st.checkbox("How can we set the caption / heading on the dataframe?"):
        st.write(data.style.set_caption('India Census 2011 Dataset'))
    
    if st.checkbox("Show the records related with the districts - New Delhi , Lucknow , Jaipur"):
        st.write(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])
    
    if st.checkbox("Calculate state-wise total number of popluation and population with different religions"):
        st.write(data.groupby('State_name').agg({'Population': 'sum', 'Hindus': 'sum', 'Muslims': 'sum', 'Christians': 'sum', 'Sikhs': 'sum', 'Buddhists': 'sum', 'Jains': 'sum'}).sort_values(by='Population', ascending=False))
    
    if st.checkbox("How many Male Workers were there in Maharashtra state ?"):
        st.write(data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum())
    
    if st.checkbox("Which state has the highest population?"):
        highest_population = data.groupby('State_name').agg({'Population': 'sum'}).sort_values(by='Population', ascending=False).head(1)
        st.write(f"{highest_population.index[0]} has the highest population of {highest_population['Population'][0]} it is beacause the no of districts in uttar pradesh is more")
    
    if st.checkbox("Show the percentages of Religions in India by a piechart"):
        st.write()
        fig = plt.figure(figsize=(10,5))
        ax1 = plt.subplot(312)
        explode = (0, 0.1, 0, 0)
        labels = ['Sikhs', 'Christians', 'Jains', 'Buddhists']
        val = [data.Sikhs.sum(),data.Christians.sum(),data.Jains.sum(),data.Buddhists.sum()]
        ax1.pie(val, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=270)
        plt.title('Pie Chart of Religions')
        st.pyplot(fig)
    
    if st.checkbox("Which state has the highest literacy rate?"):
        highest_literacy = data.groupby('State_name').agg({'Literate': 'mean'}).sort_values(by='Literate', ascending=False).head(1)
        fig = px.bar(data, x='State_name', y='Literate', title='Literacy rate by state', height=500)
        st.plotly_chart(fig)
    
    if st.checkbox("Which states have the highest number of male and female workers?"):
        workers = data.groupby('State_name').agg({'Male_Workers': 'sum', 'Female_Workers': 'sum'}).sort_values(by='Male_Workers', ascending=True).head(10)
        fig = px.bar(workers, x=workers.index, y=['Male_Workers', 'Female_Workers'], title='Number of Male and Female Workers by State', barmode='group', height=500)
        st.plotly_chart(fig)
    
    if st.checkbox("Visualize the population by state as a line chart"):
        pop_data = data.groupby('State_name').agg({'Population': 'sum'}).reset_index()
        fig = px.line(pop_data, x='State_name', y='Population', title='Line Chart Population by State')
        st.plotly_chart(fig)
    
    if st.checkbox("Histogram for showing the Age Groups"):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(data['Age_Group_0_29'], bins=10,color='skyblue',label='Age 0-29',alpha='0.5')
        ax.hist(data['Age_Group_30_49'], bins=10,color='royalblue',label='Age 30-49',alpha='0.5')
        ax.hist(data['Age_Group_50'], bins=10,color='blue',label='Age 50',alpha='0.5')
        ax.set_title('Histogram of Age Group Population')
        ax.set_xlabel('Total Population')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)