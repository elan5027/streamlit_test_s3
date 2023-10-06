import streamlit as st
import os
import boto3
import re
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
#from streamlit_option_menu import option_menu
DATA_URL = "https://ecocanvas-s3.s3.ap-northeast-2.amazonaws.com/TEST.png"
st.image(DATA_URL)
st.info("파일선택")
save_file = r'./upload/file'
pdf = st.file_uploader(label='Drag the PDF file here. Limit 100MB')
file_path = None
if pdf is not None:
        file_name = pdf.name
        match = re.search(r'\d+', file_name)
        file_path = os.path.join(save_file, file_name)
        with open(file_path, "wb") as f:
            f.write(pdf.read())
        st.success("WAV 파일 업로드 완료")
st.info(file_path)

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
    st.info(file_path)
    st.info(type(pdf))
    
    pdf.seek(0)
    name = "TEST" + str(id) + ".wav"
    st.info(name)
    s3.upload_file(file_path, bucket_name, name)
with st.sidebar:
    st.info("TEST Sidebar")

    