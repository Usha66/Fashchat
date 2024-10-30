from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()  

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load and setup the uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to analyze the fashion input
def get_fashion_analysis(image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if image:  # If image is provided, include it in the generation content
        response = model.generate_content([image[0], prompt])
    else:  # Otherwise, only use the prompt for content generation
        response = model.generate_content([prompt])
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="FashChat: Your Timeless Fashion Analyzer")

# Display the logo
logo = Image.open(r"C:\Users\usha\Downloads\lo.png")  # Ensure this path points to your logo image

# Use markdown to display the logo and title next to each other
col1, col2 = st.columns([2, 6])  # Adjust the ratios as needed
with col1:
    st.image(logo, width=150)  # Adjust width as necessary
with col2:
    st.markdown("<h1 style='margin:0;'>Your Timeless Fashion Analyzer</h1>", unsafe_allow_html=True)


analysis_type = st.selectbox("Choose an analysis type:", 
                              [
                                  "Outfit Analyzer",
                                  "Makeup Look Insights",
                                  "Movie/Celebrity Fit Analyze"
                              ])

# Handle Outfit Analyzer
if analysis_type == "Outfit Analyzer":
    st.subheader("Outfit Analysis")
    uploaded_file = st.file_uploader("Upload an image of an outfit...", type=["jpg", "jpeg", "png"])
    prompt = st.text_input("Enter your analysis prompt (optional): ")

    # Analysis options
    analysis_options = st.multiselect("Select analysis options:", 
                                       [
                                           "Trendiness Check",
                                           "Outfit Combinations",
                                           "Styling Tips",
                                           "Color Coordination Advice",
                                           "Accessory Recommendations"
                                       ])

    if st.button("Analyze Outfit"):
        if uploaded_file is not None:
            try:
                image_data = input_image_setup(uploaded_file) 
                input_prompt = f"""
                You are a fashion expert. Analyze the uploaded image and provide the following insights:
                - Selected Analysis Options: {', '.join(analysis_options)}
                - Additional prompt: {prompt}
                """
                response = get_fashion_analysis(image=image_data, prompt=input_prompt)
                st.subheader("Analysis Result")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload an image.")

# Handle Makeup Look Insights
elif analysis_type == "Makeup Look Insights":
    st.subheader("Makeup Look Analysis")
    uploaded_file = st.file_uploader("Upload an image for makeup analysis...", type=["jpg", "jpeg", "png"])
    prompt = st.text_input("Enter your makeup analysis prompt: ")

    if st.button("Analyze Makeup"):
        if uploaded_file is not None:
            try:
                image_data = input_image_setup(uploaded_file) 
                input_prompt = f"""
                You are a makeup artist. Analyze the uploaded image and provide detailed makeup insights:
                - Additional prompt: {prompt}
                """
                response = get_fashion_analysis(image=image_data, prompt=input_prompt)
                st.subheader("Makeup Insights Result")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload an image.")

# Handle Movie/Celebrity Fit Analyze
elif analysis_type == "Movie/Celebrity Fit Analyze":
    st.subheader("Movie/Celebrity Fit Analysis")
    movie_name = st.text_input("Enter the movie name: ")
    character_name = st.text_input("Enter the character name (optional): ")
    uploaded_file = st.file_uploader("Upload an image of the character or outfit...", type=["jpg", "jpeg", "png"])

    # Analysis options for movie/celebrity fits
    analysis_options = st.multiselect("Select analysis options:", 
                                       [
                                           "Outfit Analysis",
                                           "Makeup Analysis",
                                           "Trend Analysis",
                                           "Comparison to Celebrity Styles",
                                           "Outfit Availability Suggestions"
                                       ])

    if st.button("Analyze Movie/Celebrity Fit"):
        if movie_name or uploaded_file is not None:
            try:
                image_data = input_image_setup(uploaded_file) if uploaded_file is not None else None
                input_prompt = f"""
                You are a style analyst. Analyze the outfits from the movie '{movie_name}' and provide the following insights:
                - Character: {character_name if character_name else 'N/A'}
                - Selected Analysis Options: {', '.join(analysis_options)}
                """
                response = get_fashion_analysis(image=image_data, prompt=input_prompt)
                st.subheader("Movie/Celebrity Fit Analysis Result")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide either a movie name or an image.")
