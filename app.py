import streamlit as st
#from streamlit_option_menu import option_menu
from st_files_connection import FilesConnection


conn = st.experimental_connection('s3', type=FilesConnection)
st.info(conn)
df = conn.read("TEST.png", input_format="png", ttl=600)

st.info("파일선택")

with st.sidebar:
    st.info("TEST Sidebar")

    