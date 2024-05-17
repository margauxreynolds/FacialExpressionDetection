import streamlit as st
from PIL import Image
import os
import pandas as pd

from hume_util import get_facial_analytics


# Main title
st.title("📊 Facial Expression Analyzer 😊")

# Side bar title
st.sidebar.title("Image Analyzer")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

def display_emotion_data(data):

    try:

        predictions = data[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]

        emotions = predictions['emotions']
        emotion_df = pd.DataFrame(emotions).sort_values(by='score', ascending=False)

        #t.title("Emotion Analysis Results")
        #st.image(data[0]['source']['filename'], caption='Uploaded Image', use_column_width=True)
        st.subheader("Detected Emotions and Scores")
        st.table(emotion_df)

    except KeyError as e:

        st.error(f"Error: Missing key in the data structure: {e}")

    except Exception as e:

        st.error(f"An unexpected error occurred: {e}")

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = "temp_images"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    image_path = os.path.join(temp_dir, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.image(Image.open(image_path), caption='Uploaded Image.', use_column_width=True)
    if st.sidebar.button("Analyze"):
        result = get_facial_analytics(image_path)
        display_emotion_data(result)
