import pandas as pd
import streamlit as st
df= pd.read_csv("assignment/databw.csv", sep=",")
print(df)
st.header("Pam Company Limited")
st.write("The company is about dealing with Software")
st.subheader("Team Members")
col1, col2, col3=st.columns([1.5,1.5,1.5])
with col1:
    for index, row in df[:4].iterrows():
        st.write(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row["role"])
        st.image("im/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.write(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row["role"])
        st.image("im/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.write(f"{row['first name'].title()} {row['last name'].title()} ")
        st.write(row["role"])
        st.image("im/"+row["image"])