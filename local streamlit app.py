# import streamlit as st
# from fastai.vision.all import *
# from PIL import Image
# import tensorflow as tf
# import os

# # Load your trained model
# def load_model(model_path):
#     learn = load_learner(model_path)
#     return learn
    


# # Predict the category of the car
# def predict(model, img):
#     pred, _, _ = model.predict(img)
#     return pred

# # Streamlit UI
# def main():
#     st.title("F1 Car Classifier")
#     st.write("Upload an image of an F1 car to classify it.")

#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
#     if uploaded_file is not None:
#         img = Image.open(uploaded_file).convert('RGB')
#         st.image(img, caption='Uploaded Image', use_column_width=True)
#         st.write("")
#         st.write("Classifying...")

#         # Make prediction
#         model = load_model("./resnet34-stage-2.pkl")
#         prediction = predict(model, img)
#         st.write(f"Prediction: {prediction}")

        

# if __name__ == "__main__":
#     main()


import streamlit as st
from fastai.vision.all import *
from PIL import Image

# Function to load the model, using Streamlit's session state to cache the model
def load_model(model_path):
    if 'model' not in st.session_state:
        st.session_state.model = load_learner(model_path, cpu=True)
    return st.session_state.model

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
                model = load_model("./resnet34-stage-2.pkl")
                prediction, confidence = predict(model, img)
                st.write(f"Prediction: {prediction}")
                st.write(f"Confidence: {confidence:.4f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
