import cv2

# Haarcascade model load
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
from tkinter import filedialog, Tk
import cv2

def upload_image():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

image_path = upload_image()
image = cv2.imread(image_path)
def detect_smile(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=20)
    return len(smiles)  # Number of smiles detected

smile_count = detect_smile(image)
smile_ratio = min(smile_count, 5)  # Max ratio 5 tak
print(f"Smile Rating: {smile_ratio}/5")
import tkinter as tk

def display_result(rating):
    root = tk.Tk()
    root.title("Smile Rating")
    tk.Label(root, text=f"Smile Rating: {rating}/5", font=("Helvetica", 16)).pack()
    root.mainloop()

display_result(smile_ratio)
import streamlit as st

st.title("Smile Rating App")
uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    smile_ratio = detect_smile(image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write(f"Smile Rating: {smile_ratio}/5")



