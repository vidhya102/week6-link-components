import streamlit as st
import numpy as np
from PIL import Image, ImageOps

# -------------------------------------------------
# Dummy prediction function (since TF is removed)
# -------------------------------------------------
def predict_digit(img_arr):
    # This is a dummy prediction – always returns 7 (for demo)
    return 7

# -------------------------------------------------
# Streamlit Page Setup
# -------------------------------------------------
st.set_page_config(page_title="Handwritten Digit Predictor", layout="centered")

st.title("📝 Handwritten Digit Classifier")
st.write("Upload an image of a handwritten digit (0–9) to test the model.")

st.divider()

# -------------------------------------------------
# Upload Image
# -------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=250)

    # Preprocess image
    img = ImageOps.grayscale(img)
    img = img.resize((28, 28))
    img_arr = np.array(img) / 255.0
    img_arr = img_arr.reshape(1, 28, 28, 1)

    st.write("🔍 Processing image...")

    # -------------------------------------------------
    # Predict (Dummy)
    # -------------------------------------------------
    result = predict_digit(img_arr)
    st.success(f"Predicted digit: **{result}**")
else:
    st.info("Please upload an image to continue.")



