import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Handwritten Digit Predictor", layout="centered")

# ----------- HEADER -------------
st.title("🧮 Handwritten Digit Classifier (Demo)")
st.write("Upload an image of a handwritten digit (0–9) to test the model.")

st.divider()

# ----------- IMAGE UPLOAD -------------
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=250)

    st.divider()

    if st.button("Predict"):
        with st.spinner("Analyzing the image..."):
            # FAKE result for Week 7 (dummy output)
            predicted_class = "Dog"
            confidence = 87.0

        st.success(f"Predicted Class: **{predicted_class}**")
        st.metric("Confidence Score", f"{confidence}%")

else:
    st.info("Please upload an image to begin.")

st.write("---")
st.caption("Week 7 – UI Refinement & Deployment Task | DIY Internship")
