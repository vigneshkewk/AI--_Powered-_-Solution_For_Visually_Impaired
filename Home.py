import streamlit as st

def app():
    st.title("👁‍🗨 AI ASSISTANT")
    st.subheader("An AI-Powered Solution for the Visually Impaired")
    
    st.markdown("""
    ### Features:
    - 🔍 **Describe Scene**: Get detailed descriptions of images.
    - 📝 **Extract Text**: Extract text from images using OCR.
    - 🔊 **Text-to-Speech**: Convert extracted text to speech.

    ### How to Use:
    - Click one of the buttons below to explore the feature.
    """)

    # Navigation buttons
    if st.button("🔍 Describe Scene"):
        st.session_state.page = "Describe Scene"

    if st.button("📝 Extract Text"):
        st.session_state.page = "Extract Text"

    if st.button("🔊 Text-to-Speech"):
        st.session_state.page = "Text-to-Speech"
