import streamlit as st
from fastai.vision.all import *
from PIL import Image
import tensorflow as tf
import os

# Load your trained model
def load_model(model_path):
    learn = load_learner(model_path)
    return learn
    


# Predict the category of the car
def predict(model, img):
    pred, _, _ = model.predict(img)
    return pred

# Streamlit UI
def main():
    st.title("F1 Car Classifier")
    st.write("Upload an image of an F1 car to classify it.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert('RGB')
        st.image(img, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Make prediction
        model = load_model("./resnet34-stage-2.pkl")
        prediction = predict(model, img)
        st.write(f"Prediction: {prediction}")

        

if __name__ == "__main__":
    main()
