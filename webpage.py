import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
#creating image and info column
col1, col2=st.columns(2)
with col1:
    col1=st.image("image/photo1.png",width=300)
#My info
with col2:
    col2=st.title("Joseph Otoo Amoah")
    content=""" Hi, I am Joseph! I am an Economist, a Python programmer, data analyst, and financial analyst.
     I am currently pursing  MSc Economics at Friedrich-Schiller University of Jena,
     specialising in quantitative macroeconomics.
     I graduated in 2021 with a bachelor degree in Economics with Statistics from University of Ghana.
     I am very conversant and experienced in econometric software such Python, Rstudio,Stata, and Microsoft office.
     I have worked with institution like Ghana Revenue Authority as service personnel.
     I am always eager to learn, and come out with innovative ideas. 
    """
    st.info(content)
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

# Creating another columns for apps
df=pd.read_csv("data.csv",sep=";")
col3,col4=st.columns(2)
with col3:
    for index,row in df[0:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])