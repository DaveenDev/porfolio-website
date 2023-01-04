import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content="""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis maximus quam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut vitae maximus ipsum. Phasellus eu enim cursus, facilisis sem a, cursus quam. Nam eget facilisis ipsum, et laoreet augue. Morbi vestibulum ornare ex, sed venenatis ligula. In ornare tempus metus, vel blandit ante ultricies vehicula. Cras imperdiet sapien at libero convallis, nec tincidunt felis gravida. Curabitur malesuada consectetur feugiat. Praesent luctus porta hendrerit. Mauris ac tempus ex, a mattis turpis. Sed aliquam lobortis metus, nec viverra dui. Donec commodo sed turpis sit amet auctor. 
    """
    st.info(content)


st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

r2_col1, r2_col2 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with r2_col1:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with r2_col2:
    for index, row in df[10:].iterrows():
        st.header(row["title"])