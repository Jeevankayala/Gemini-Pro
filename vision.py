from dotenv import load_dotenv
load_dotenv()     ## loading all environmental variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("Google_API_KEY"))
model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Image Demo")

st.header("Gemini Application")

input=st.text_input("Input:  ",key="input")

# Add a file uploader widget to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit=st.button("Describe the image")

## when submit is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("This is the reponse")
    st.write(response)

