import streamlit as st
import os
import boto3
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
#from streamlit_option_menu import option_menu
DATA_URL = "https://ecocanvas-s3.s3.ap-northeast-2.amazonaws.com/TEST.png"
st.image(DATA_URL)
st.info("파일선택")

pdf = st.file_uploader(label='Drag the PDF file here. Limit 100MB')
if pdf is not None:
    s3 = boto3.client(
        service_name='s3',
        region_name=st.secrets["AWS_DEFAULT_REGION"] ,
        aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"] ,
        aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"] ,
    )
    st.info(s3)
    
    id = 123
    bucket_name = 'ecocanvas-s3'
    print(pdf)
    print(type(pdf))
    pdf.seek(0)
    name = "pdf_" + str(id) + ".pdf"
    print(name)
    s3.upload_file(pdf, bucket_name, name)
with st.sidebar:
    st.info("TEST Sidebar")

    