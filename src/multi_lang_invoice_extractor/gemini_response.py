import dotenv
import os
import sys
from src.exception import CustomException
from src.logger import logging
import google.generativeai as genai

# Load the environment variables from the .env file
dotenv.load_dotenv()

#configure google api
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load Gemini-pro-vision model and get respones
def get_gemini_response(input,image,prompt):
    """
    Generates a response using the Gemini generative model.

    Args:
        input_text (str): The text input to be used for generating the response.
        image (list, optional): A list containing the image data. If provided,
            it will be used as additional input for the model. Defaults to None.
        prompt (str, optional): An optional prompt to guide the model's
            generation process. Defaults to None.

    Returns:
        str: The generated response from the Gemini model.

    Raises:
        CustomException: If an error occurs during generation.
    """
    try:
        logging.info("Loading INTO gemini response...")
        
        # Create the generative model instance
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content([input,image[0],prompt])
        return response.text

    except Exception as e:
        logging.info("Error Occured while getting gemini response")
        raise CustomException(e,sys)