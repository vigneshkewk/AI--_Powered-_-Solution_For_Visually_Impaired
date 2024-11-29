import streamlit as st
import google.generativeai as genai

def generate_scene_description(input_prompt, image_data):
    """Generates a scene description using Google Generative AI."""
    API_KEY = "AIzaSyABPT0_XBjWGkrNLR8MdH_wwnx7QlA-KJo"
    genai.configure(api_key=API_KEY)     
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input_prompt, image_data[0]])
    return response.text

def input_image_setup(uploaded_file):
    """Prepares the uploaded image for processing."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded.")

def app():
    st.title("🔍 Describe Scene")
    st.write("Upload an image to generate a detailed scene description.")

    input_prompt = """
                    As an AI assistant, your task is to assist visually impaired users by describing the contents of the uploaded image. Please provide:
                    1. A list of key objects identified in the image along with their function or significance.
                    2. A detailed description of the scene.
                    3. Practical suggestions for actions or safety precautions that the visually impaired person should consider in this environment.
                    """


    uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        with st.spinner("Processing image..."):
            image_data = input_image_setup(uploaded_file)
            response = generate_scene_description(input_prompt, image_data)
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            st.markdown("### Generated Scene Description")
            st.write(response)

    # Back to Home Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
