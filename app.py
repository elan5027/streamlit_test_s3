import streamlit as st
import os
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.


script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
#from streamlit_option_menu import option_menu

st.info("파일선택")
pdf = st.file_uploader(label='Drag the PDF file here. Limit 100MB')

conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("ecocanvas-s3/Delay_Prob.csv", input_format="csv", ttl=600)

# for row in df.itertuples():
#     st.write(f"{row.Owner} has a :{row.Pet}:")

with st.sidebar:
    st.info("TEST Sidebar")

