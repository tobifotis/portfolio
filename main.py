import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tobi Emmanuel")
    content = """
    Hi, I am Tobi! I am an aspiring developer and currently a full-time student.
    I am a junior studying computer science at the University of North Texas.
    In my free time, I enjoy learning new technologies, building projects, and playing soccer.
    """
    st.info(content)