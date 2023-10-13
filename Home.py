import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/119FP0988cropped1.jpeg", width= 500)

with col2:
    st.title("Arpan Swain")
    content = """
As a dedicated data science enthusiast with a strong foundation in SQL and Python, I am deeply passionate about the field of machine learning. Through a series of individual projects, I have harnessed my skills to explore data, build models, and extract insights, reinforcing my commitment to this dynamic discipline.
I am eager to expand my expertise, delve deeper into the world of data science, and contribute to meaningful, data-driven solutions. My website(also built by me) showcases the culmination of my efforts, featuring a selection of projects that highlight my proficiency 

I am excited to continue my learning journey, engage with fellow data science enthusiasts, and explore opportunities to make a significant impact in this ever-evolving field.






"""


    st.info(content)

content2 = """
Take a look at my Projects. Feel free to check and You can contact me also !! see you in my mailbox.. Have a Good Day!
"""
st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data2.csv",sep = ";")

with col3:
    for index,rows in df[:5].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image(f"images/{rows['image']}")
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index,rows in df[5:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image(f"images/{rows['image']}")
        st.write(f"[Source Code]({rows['url']})")