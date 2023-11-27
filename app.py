import streamlit as st
import os
from PIL import Image
import streamlit as st
from PIL import Image
import tempfile
from dotenv import load_dotenv
import os
from llama_index.multi_modal_llms.generic_utils import (load_image_urls)

# Setting up environment variables
load_dotenv()
open_api_key = os.environ['OPENAI_API_KEY']

## Setting the OPEN AI Vision API 

from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index import SimpleDirectoryReader

openai_mm_llm = OpenAIMultiModal(
    model="gpt-4-vision-preview",
    api_key=open_api_key,
    max_new_tokens=500,
    temperature=0.0,
)

st.title('Image Uploader and Analyzer')
st.write("Hello World")
st.write("""
# My first app
Hello *world!*
""")



uploaded_file = st.file_uploader("Choose an image...", type="jpg")
st.write("UUUPLOADED FILE")
