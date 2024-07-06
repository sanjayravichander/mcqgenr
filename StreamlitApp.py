import os
import json
import pandas as pd
import traceback
import certifi
from dotenv import load_dotenv
import streamlit as st
from langchain_community.callbacks.manager import get_openai_callback
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQgenerator import generate_eval_chain
import openai
import httpx

# Set environment variable to use the certifi certificate bundle
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load response file
with open(r"C:\Users\DELL\mcqgenr\response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

# Set logging configuration
logging.basicConfig(level=logging.INFO)

# Creating Title
st.title("MCQ Generator Application - Langchain")

# Create a form using st.form
with st.form("user_inputs"):
    # File upload
    upload_file = st.file_uploader("Upload a File (PDF/Txt)")
    # Setting up number of MCQs
    mcq_count = st.number_input("Number of MCQs", min_value=3, max_value=50)
    # Setting up Subject
    subject = st.text_input("Specify the Subject", max_chars=20)
    # Quiz Tone
    tone = st.text_input("Complexity Level", max_chars=20, placeholder="Simple")
    # Add Button
    button = st.form_submit_button("Create MCQs")

# Check if the button is clicked and all fields have input
if button and upload_file is not None and mcq_count and subject and tone:
    with st.spinner("Loading..."):
        try:
            text = read_file(upload_file)
            # Count tokens and the cost of all
            with get_openai_callback() as cb:
                response = generate_eval_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )
                logging.info(f"Generated MCQs successfully with {cb.total_tokens} tokens.")
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Error occurred while processing. Please try again.")
        else:
            if isinstance(response, dict):
                # Extract quiz data from response
                quiz = response.get("quiz", None)
                if quiz is not None:
                    table_data = get_table_data(quiz)
                    if table_data is not None:
                        df = pd.DataFrame(table_data)
                        df.index = df.index + 1
                        st.table(df)
                        # Display the review in a text box as well
                        st.text_area(label="Review", value=response["review"])
                    else:
                        st.error("Error in the table data")
                else:
                    st.write(response)
            else:
                st.error("Unexpected response format from MCQ generation.")
