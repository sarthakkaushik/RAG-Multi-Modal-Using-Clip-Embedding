import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import openai
import os

#Setting up enviorment variables
load_dotenv()
open_api_key=os.environ['OPENAI_API_KEY']
openai.api_key=open_api_key

## Setting the OPEN AI VIsion API 

from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index import SimpleDirectoryReader

openai_mm_llm = OpenAIMultiModal(
    model="gpt-4-vision-preview",
    api_key= open_api_key,
    max_new_tokens=500,
    temperature=0.0,
)

st.title('Image Uploader and Analyzer')
st.write("Hellow World")
st.write("""
# My first app
Hello *world!*
""")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    image_documents= SimpleDirectoryReader(image).load_data()
    query="Analysiz the give image"
    st.write(query)

    response = openai_mm_llm.complete(
    prompt=query,
    image_documents=image_documents,
    )
    st.write("Fetching response: ")
    st.write(response)
