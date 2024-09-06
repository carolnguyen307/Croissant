
import streamlit as st
import gdown
import os
import pandas as pd
import numpy as np
import pickle
import tempfile
from PIL import ImageFont, ImageDraw, Image
#from efficientnet.tfkeras import EfficientNetB4
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, array_to_img


# Function to download the file from Google Drive
# @st.cache_resource()
def download_file_from_drive(url, output):
    gdown.download(url, output, quiet=False)

# opening the image
# image = open('banner_image.jpeg', 'rb').read()
# st.image(image, use_column_width=True)

st.title("Croissant")
st.markdown("Predict croissant quality")

# Add a separator between the header and the main content
st.markdown("---")


# Load the trained model
#model = load_model('model.h5')
# Google Drive file link (shared link)
file_url = 'https://drive.google.com/uc?1_wYk2Zo_YkINqoRwSf3L_DUjkjHFwV08'
output_file = 'model.h5'

if "model" not in st.session_state.keys():

    download_file_from_drive(file_url, output_file)
    st.success('Model downloaded successfully!')

    # Check if the file exists
    if os.path.exists(output_file):
        # Check if the file is indeed an .h5 file by size (usually > few MBs)
        file_size = os.path.getsize(output_file)
        #st.write(f"Downloaded file size: {file_size / (1024 * 1024)} MB")
        
        if file_size > 0:  # Ensuring the file is not empty
            try:
                with st.spinner('Loading model...'):
                    st.session_state["model"] = load_model(output_file)
                    st.success('Model loaded successfully!')
                    st.write(model.summary())
            except OSError as e:
                st.error(f"Error loading model: {e}")
        else:
            st.error('Downloaded file is empty or corrupted.')
    else:
        st.error('Error: Model file not found.')

    
model = st.session_state["model"]

# Uncomment to reload the model
# del st.session_state["model"]







st.header("Upload your image")

# Get user input for image upload
uploaded_file = st.file_uploader('Upload an image of your croissant', type=['jpg', 'jpeg', 'png'])

# Process the uploaded image if it exists
if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Load new images for prediction
    new_image = image
    new_image_array = np.array(new_image.resize((384, 384)))  # Resize the image to match the model's input shape
    new_image_array = np.expand_dims(new_image_array, axis=0)  # Add batch dimension
    new_image_array = new_image_array / 255.0  # Normalize the pixel values (same as during training)

    # Make predictions
    predictions = model.predict(new_image_array)

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions, axis=1)[0]

    # Indicate class names
    class_names = ['Bad', 'Good']

    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]

    st.write(f"Your croissant is : {predicted_class_name}")


