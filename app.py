import streamlit as st

# ---- Title ----
st.title("Week 6 - Linking Input & Output Components")

st.write("This demo shows how input components connect to a prediction function.")

# ---- Input Component ----
user_input = st.text_input("Enter any text:")

# ---- Prediction Function (Fake) ----
def predict(text):
    if text.strip() == "":
        return "No input", 0.0
    return "Sample Prediction", 0.85   # fake output

# ---- Connect input → function → output ----
if st.button("Predict"):
    prediction, confidence = predict(user_input)

    st.subheader("Prediction Result")
    st.success(f"Predicted Class: {prediction}")

    st.subheader("Confidence")
    st.write(f"{confidence * 100:.2f}%")
