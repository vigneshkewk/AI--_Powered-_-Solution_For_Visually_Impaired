import streamlit as st
from PIL import Image
import pytesseract
import pyttsx3

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

rate = engine.getProperty('rate')  # Get the current speech rate
engine.setProperty('rate', rate - 50) 


def extract_text_from_image(image):
    """Extracts text from the given image using OCR."""
    return pytesseract.image_to_string(image)

def text_to_speech(text):
    """Converts the given text to speech."""
    engine.say(text)
    engine.runAndWait()

def app():
    st.title("🔊 Text-to-Speech")
    st.write("Upload an image to extract text and listen to it.")

    uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Processing..."):
            extracted_text = extract_text_from_image(image)
            if extracted_text.strip():
                st.markdown("### Extracted Text")
                st.text_area("Text Output", extracted_text, height=200)

                if st.button("🎧 Play Text-to-Speech"):
                    text_to_speech(extracted_text)
                    st.success("Audio playback completed!")
            else:
                st.warning("No text found in the image.")

    # Back to Home Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
