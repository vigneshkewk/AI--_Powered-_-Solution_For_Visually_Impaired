import streamlit as st
from PIL import Image
import pytesseract

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def extract_text_from_image(image):
    """Extracts text from the given image using OCR."""
    return pytesseract.image_to_string(image)

def app():
    st.title("📝 Extract Text")
    st.write("Upload an image to extract text using OCR.")

    uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_image(image)
            st.markdown("### Extracted Text")
            st.text_area("Text Output", extracted_text, height=200)

    # Back to Home Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
