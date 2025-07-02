
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load model
# model = load_model('face_mask_ai.keras')
import gdown


url = "https://drive.google.com/uc?id=149CwCkdKkH7B6ZAiAC_KgYmrNOGvB40n"
output = "face_mask_ai.h5"
gdown.download(url, output, quiet=False)


from tensorflow.keras.models import load_model
model = load_model("face_mask_ai.h5")


st.title("Deteksi Masker Wajah 😷")

uploaded_file = st.file_uploader("Upload Gambar Wajah", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang Diunggah', use_column_width=True)
    
    # Preprocessing
    img = image.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prediksi
    prediction = model.predict(img_array)[0][0]
    
    # Interpretasi
    if prediction < 0.5:
        st.error("❌ Tanpa Masker")
    else:
        st.success("✅ Dengan Masker")
