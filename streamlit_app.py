

import streamlit as st
from fastai.vision.all import *
from PIL import Image

from pathlib import Path

# def load_model(model_path):
#     # Ensure the model_path is a Path object, which automatically handles cross-platform path formatting
#     model_path = Path(model_path)
#     path_str = str(model_path)
    
#     if 'model' not in st.session_state:
#         st.session_state.model = load_learner(path_str, cpu=True)
#     return st.session_state.model

# Load your trained model
def load_model(model_path):
    model_path = Path(model_path)
    path_str = str(model_path)
    learn = load_learner(path_str)
    return learn

# Function to preprocess the image
def preprocess_image(img, target_size=(224, 224)):
    return img.resize(target_size)

# Function to predict the category of the car
def predict(model, img):
    img = preprocess_image(img)  # Preprocess the image
    pred, pred_idx, probs = model.predict(img)
    return pred, probs[pred_idx]

# Streamlit UI
def main():
    st.title("F1 Car Classifier")
    st.write("Upload an image of an F1 car to classify it.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file).convert('RGB')
            st.image(img, caption='Uploaded Image', use_column_width=True)

            with st.spinner('Classifying...'):
                model = load_model("./f1_model.pkl")
                prediction, confidence = predict(model, img)
                st.write(f"Prediction: {prediction}")
                st.write(f"Confidence: {confidence:.4f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
