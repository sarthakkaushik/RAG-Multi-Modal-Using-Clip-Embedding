import os
from dotenv import load_dotenv
import openai
from PIL import Image
import matplotlib.pyplot as plt

from llama_index.prompts import PromptTemplate
from llama_index.query_engine import SimpleMultiModalQueryEngine

from llama_index.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.vector_stores import QdrantVectorStore
from llama_index import SimpleDirectoryReader, StorageContext
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.response.notebook_utils import display_source_node



import qdrant_client

from PIL import Image
import matplotlib.pyplot as plt
import os
import random


#Setting up enviorment variables
from dotenv import load_dotenv
import os
import openai
load_dotenv()
# openai.api_key= os.environ['OPENAI_API_KEY']

openai.api_key= os.environ['OPENAI_API_KEY']



def create_qdrant_vdb(dir_path):
    
    # Create a local Qdrant vector store
    # Generate a random integer between 1 and 1000 (inclusive)
    random_number = random.randint(1, 1000)
    save_path=f'qdrant_mm_db_{random_number}'
    client = qdrant_client.QdrantClient(path=save_path)

    text_store = QdrantVectorStore(
        client=client, collection_name="text_collection"
    )
    image_store = QdrantVectorStore(
        client=client, collection_name="image_collection"
    )
    storage_context = StorageContext.from_defaults(vector_store=text_store)

    # Create the MultiModal index
    documents = SimpleDirectoryReader(dir_path).load_data()
    index = MultiModalVectorStoreIndex.from_documents(
        documents, storage_context=storage_context, image_vector_store=image_store
    )
        
    # Save it
    # index.storage_context.persist(persist_dir="./Multimodel_storage")
    
    return index
    

def Create_Query_Engine(index):
    
    qa_tmpl_str = (
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the query.\n"
        "Query: {query_str}\n"
        "Answer: "
    )
    qa_tmpl = PromptTemplate(qa_tmpl_str)
    openai_mm_llm = OpenAIMultiModal()

    query_engine = index.as_query_engine(
        multi_modal_llm=openai_mm_llm, text_qa_template=qa_tmpl
    )
    
    return query_engine

def get_response(query_engine, query_ques):
    
  
    response = query_engine.query(query_ques)
    res_text=str(response)
    
    return res_text
        