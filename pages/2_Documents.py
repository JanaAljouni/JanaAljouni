import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")



st.title("💻 Documents")
st.write('Below you can find all the downloadable documents')


with open("images/resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open("images/GP1.pdf", "rb") as pdf_file:
    PDFbyte1 = pdf_file.read()

with open("images/Transcript .pdf", "rb") as pdf_file:
    PDFbyte2 = pdf_file.read()

with open("images/Degree_of_honor.pdf", "rb") as pdf_file:
    PDFbyte3 = pdf_file.read()



st.download_button(
    label="Resume",
    data=   PDFbyte ,
    file_name="resume.pdf",
    mime="application/octet-stream",
)


st.download_button(
    label="Quantum Analyzer doc",
    data=PDFbyte1,
    file_name="Quantum.pdf",
    mime="application/octet-stream",
)

st.download_button(
    label="Transcript",
    data=PDFbyte2,
    file_name="Transcript.pdf",
    mime="application/octet-stream",
)

st.download_button(
    label="Degree of Honor",
    data=PDFbyte3,
    file_name="degree_of_honor",
    mime="application/octet-stream",
)

