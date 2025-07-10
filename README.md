# 😷 Mask Detection App

The **Mask Detection App** is a web-based application designed to detect whether a person in an uploaded image is wearing a face mask or not. It uses a deep learning model, specifically a Convolutional Neural Network (CNN), trained to classify images into two categories: “with mask” and “without mask.” The goal of this project is to apply computer vision in a real-world scenario, particularly in the context of health and safety.

This project was inspired by [PhilipPurwoko's Face-Mask-Detection repository](https://github.com/PhilipPurwoko/Face-Mask-Detection), which provided a foundational understanding of model training and mask classification using deep learning. The current project builds upon that work by extending it with a user-friendly web interface using Streamlit and a deployment setup using Streamlit Cloud for public access.

The project is built using the **Python programming language** and utilizes the **Streamlit** library to create a clean and interactive user interface. The model is trained using **TensorFlow/Keras** and hosted externally via **Google Drive**, allowing the application to download and load the model during runtime without embedding large files in the repository. The web application is deployed using **Streamlit Cloud**, making it accessible directly from a browser without any setup.

The main benefits of this project are to demonstrate the use of deep learning for public health monitoring and to provide an educational example of deploying an AI model as a web application. It shows how machine learning can be integrated into user-friendly tools that solve real-world problems and can be used as a learning reference for students or developers.

The app allows users to upload an image of a person’s face, and within seconds, it provides a prediction on whether the person is wearing a mask. The interface is simple and requires no technical knowledge to use. The model architecture includes convolutional layers for feature extraction, followed by dense layers for classification, with sigmoid activation at the output to determine the class.

---
## Dataset
I got the dataset from Kaggle (https://www.kaggle.com/omkargurav/face-mask-dataset). The data consists of 7553 photos. The photos are .jpg with 3 channels (RGB). 3725 face photos with masks and 3828 face photos without masks with various photo sizes.


## 🚀 Features

- Upload image via web interface
- Detects whether the person is wearing a face mask
- Displays result instantly with visual feedback
- Loads model externally to reduce repo size
- Easy deployment via Streamlit Cloud

---

## 🛠 Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- Google Drive (for model storage)
- Git & GitHub (version control and deployment)

---

## 📁 Folder Structure

mask-detection-app/
│
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
├── .gitignore # Files/folders to ignore in Git
├── README.md # Project description
└── assets/ (optional) # Folder for image assets, logos, etc.


---

🌐 Deploy on Streamlit Cloud
1. Push your project to a public GitHub repository.
2. Go to streamlit.io/cloud and sign in.
3. Click "New app", choose the repository and the app.py file.
4. Click "Deploy".

---

## ⚠️ Limitations

While the Mask Detection App is functional and demonstrates the integration of deep learning with a web interface, it has several limitations:

- **Model Size and Loading Time:** The trained model (.h5 file) is over 100MB in size, which causes a noticeable delay when the app loads, especially on first launch or on slower internet connections.
- **Limited Dataset:** The model was trained on a relatively small and specific dataset, which may lead to reduced accuracy when tested on real-world images with different lighting, angles, or backgrounds.
- **No Real-Time Detection:** The app only works on static images. It does not support real-time webcam input or video-based detection, which limits its practical use in dynamic environments.
- **Binary Classification Only:** The model only distinguishes between two classes: “with mask” and “without mask.” It does not detect incorrect mask usage (e.g., nose uncovered).
- **No User Feedback or Logging:** There is no mechanism for users to provide feedback on incorrect predictions, nor is there a logging system to collect data for further training or improvement.

Despite these limitations, the app serves well as a proof of concept and educational project. Future iterations could address these issues by improving dataset quality, optimizing the model size, and expanding the feature set.

