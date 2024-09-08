import streamlit as st
import requests
import os
import pandas as pd
import numpy as np
import pickle
import tempfile
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, array_to_img


# Function to download the model from OneDrive
def download_file_from_onedrive(one_drive_link):
    # Modify the OneDrive link to enable direct download
    direct_download_link = one_drive_link.replace("redir?", "download?")
    
    # Send an HTTP request to download the file
    response = requests.get(direct_download_link)
    
    # Ensure the request was successful
    if response.status_code == 200:
        # Create a temporary file
        temp_model_file = tempfile.NamedTemporaryFile(delete=False, suffix='.h5')
        # Write the content to this temp file
        temp_model_file.write(response.content)
        temp_model_file.close()
        return temp_model_file.name
    else:
        st.error("Failed to download the file. Check the link.")
        return None

st.title("Croissant")
st.markdown("Predict croissant quality")

# Add a separator between the header and the main content
st.markdown("---")

# OneDrive file link (shared link)
file_url = 'https://1drv.ms/u/s!Ao5lMwzKXu6xhcVwBaoS50EPZ9G1cw?e=4xcIS3'
output_file = 'model.h5'

if "model" not in st.session_state.keys():
    # Download the model file from OneDrive
    output_file = download_file_from_onedrive(file_url)
    
    if output_file:
        st.success('Model downloaded successfully!')

        # Check if the file exists and is not empty
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            
            if file_size > 0:
                try:
                    with st.spinner('Loading model...'):
                        st.session_state["model"] = load_model(output_file)
                        st.success('Model loaded successfully!')
                        st.write(st.session_state["model"].summary())
                except OSError as e:
                    st.error(f"Error loading model: {e}")
            else:
                st.error('Downloaded file is empty or corrupted.')
        else:
            st.error('Error: Model file not found.')

# Load the model from session state
model = st.session_state["model"]

# Header for image upload
st.header("Upload your image")

# Get user input for image upload
uploaded_file = st.file_uploader('Upload an image of your croissant', type=['jpg', 'jpeg', 'png'])

# Process the uploaded image if it exists
if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Load and preprocess the uploaded image for prediction
    new_image = image
    new_image_array = np.array(new_image.resize((384, 384)))  # Resize the image to match the model's input shape
    new_image_array = np.expand_dims(new_image_array, axis=0)  # Add batch dimension
    new_image_array = new_image_array / 255.0  # Normalize pixel values (as during training)

    # Make predictions
    predictions = model.predict(new_image_array)

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions, axis=1)[0]

    # Indicate class names
    class_names = ['Bad', 'Good']

    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]

    st.write(f"Your croissant is: {predicted_class_name}")
