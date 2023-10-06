import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Menu", ["테스트옵션001", "테스트옵션002"], menu_icon="cast", default_index=0, styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"}})
    