import streamlit as st

# ---- Week 3: Prediction Function (Fake Example) ----
def predict(image):
    # Use your real model later
    return "Dog", 0.87  


# ---- Week 4: Input Components ----
st.title("Week 6 - Link Components with Prediction Function")
st.write("Upload an image and get the model prediction.")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])


# ---- Week 5: Output Components ----
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", width=250)

    if st.button("Predict"):
        label, confidence = predict(uploaded_image)

        st.subheader("Prediction Result")
        st.success(f"Predicted Class: {label}")

        st.subheader("Confidence Score")
        st.write(f"{confidence*100:.2f}%")

