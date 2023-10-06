import streamlit as st
#from streamlit_option_menu import option_menu
DATA_URL = "https://ecocanvas-s3.s3.ap-northeast-2.amazonaws.com/TEST.png"
st.image(DATA_URL)
st.info("파일선택")

with st.sidebar:
    st.info("TEST Sidebar")

    