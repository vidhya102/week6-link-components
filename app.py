import streamlit as st
import numpy as np
from PIL import Image, ImageOps

# Page settings
st.set_page_config(page_title="Handwritten Digit Predictor", layout="centered")

# Header
st.title("🖐️ Handwritten Digit Classifier")
st.write("Upload an image of a handwritten digit (0–9) to test the model.")

st.divider()

# Load model once
model = load_model("mnist_model.h5")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=250)
    st.divider()

    if st.button("Predict"):
        with st.spinner("Analyzing the image..."):
            
            # Convert to grayscale and resize to 28x28
            img_gray = img.convert("L").resize((28, 28))

            # Convert to array and scale
            img_arr = np.array(img_gray).astype("float32") / 255.0

            # Invert (MNIST is white digit on black background)
            img_arr = 1.0 - img_arr

            # Reshape for model input
            img_arr = img_arr.reshape(1, 28, 28, 1)

            # Prediction
            preds = model.predict(img_arr)
            predicted_class = int(np.argmax(preds))
            confidence = float(np.max(preds)) * 100

        st.success(f"Predicted Class: **{predicted_class}**")
        st.metric("Confidence Score", f"{confidence:.2f}%")


