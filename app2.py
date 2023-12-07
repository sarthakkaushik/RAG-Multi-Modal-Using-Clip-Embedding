import streamlit as st
from multimodel import create_qdrant_vdb,Create_Query_Engine,get_response
from dotenv import load_dotenv
import openai
import os
#Setting up enviorment variables

st.title("File Path Input")

# Create a text input field for the file path
file_path = st.text_input("Enter Directory path:", placeholder="e.g., /path/to/dir")

if file_path:
    # Print the file path
    st.write("Dir path:", file_path)
    
# with st.spinner("Creating vector db.......please wait for some time"):
#     index=create_qdrant_vdb(file_path)
# st.success("Index created")

# query_ques=st.chat_input("Enter the question")
# qe=Create_Query_Engine(index)
# res=get_response(qe,query_ques)

# st.write(res)