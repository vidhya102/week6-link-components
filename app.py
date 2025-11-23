from tensorflow.keras.models import load_model
import numpy as np
from PIL import ImageOps

# load model once
model = load_model("mnist_model.h5")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=250)
    st.divider()

    if st.button("Predict"):
        with st.spinner("Analyzing the image..."):

            # convert to grayscale and resize to 28x28
            img_gray = img.convert("L").resize((28, 28))

            # convert to array
            img_arr = np.array(img_gray).astype("float32") / 255.0

            # invert colors for MNIST (white digit on black background)
            img_arr = 1.0 - img_arr

            # reshape for model
            img_arr = img_arr.reshape(1, 28, 28, 1)

            # prediction
            preds = model.predict(img_arr)
            predicted_class = int(np.argmax(preds))
            confidence = float(np.max(preds)) * 100

        st.success(f"Predicted Class: **{predicted_class}**")
        st.metric("Confidence Score", f\"{confidence:.2f}%\")

