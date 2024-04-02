import os
import sys
import streamlit as st
import pathlib
import textwrap
from PIL import Image
from src.exception import CustomException
from src.logger import logging
from src.multi_lang_invoice_extractor.gemini_response import get_gemini_response
from src.multi_lang_invoice_extractor.input_img import input_image_setup
from src.utils import set_background
from prompt_templates.prompt import PROMPT

set_background("C:\\Users\\yahia\\OneDrive\\Desktop\\background.jpg")
##initialize our streamlit app
def main():

    logging.info("Starting streamlit....")
    try:
        #st.set_page_config(page_title="Gemini Invoice Extractor")
        st.header("Mult Language Invoice Extractor Version")

        input = st.text_input("Input Prompt: ",key="input")

        uploaded_file = st.file_uploader("Choose An Image...",
                                         type = ["jpg", "png","jpeg"])
        
        image = ""

        if uploaded_file is not None:

            image = Image.open(uploaded_file)
            st.image(
                image,
                caption="Uploaded Image",
                use_column_width=True)
            
        submit = st.button("Tell Me About Image")

        input_prompt = PROMPT

        ## If ask button is clicked

        if submit:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt,image_data,input)
            st.subheader("The Response is")
            st.write(response)
    
    except Exception as e:
        logging.info("Error Occured in streamlit app.py")
        raise CustomException(e,sys)
    
if __name__ == "__main__":
        main()