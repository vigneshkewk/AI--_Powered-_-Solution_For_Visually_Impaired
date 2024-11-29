import streamlit as st
from Home import app as home_page
from scene_describer import app as describe_scene_page
from text_extractor import app as text_extract_page
from text_to_speech import app as text_to_speech_page


# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navigation logic
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Describe Scene":
    describe_scene_page()  # Pass API key only here
elif st.session_state.page == "Extract Text":
    text_extract_page()
elif st.session_state.page == "Text-to-Speech":
    text_to_speech_page()
