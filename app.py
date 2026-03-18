# Import necessary libraries and modules for the Streamlit app, 
# including the AI detector, humanizer, and utility functions
import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

import streamlit as st
from detector import load_detector, detect_ai
from humanizer import load_humanizer, humanize_text
from utils import plot_pie, word_count

# Set Streamlit page configuration for better layout and title
st.set_page_config(page_title="AI Detector & Humanizer", layout="wide")

# Main title of the app
st.title("🧠 AI Content Detector + Humanizer")

# Sidebar controls
st.sidebar.header("⚙️ Settings")

# Allow users to set maximum input and output word limits 
# for better performance and readability
max_input_words = st.sidebar.slider(
    "Maximum Input Words",
    min_value=50,
    max_value=1000,
    value=300
)

# Allow users to set maximum output words for the humanized text
max_output_words = st.sidebar.slider(
    "Humanized Output Word Limit",
    min_value=50,
    max_value=500,
    value=150
)


# Load models with caching to improve performance and avoid reloading on every interaction
@st.cache_resource
def load_models():
    detector = load_detector()
    tokenizer, model = load_humanizer()
    return detector, tokenizer, model

detector, tokenizer, model = load_models()


# Input area for users to paste their text for analysis and humanization
text = st.text_area("📄 Paste your text here:")

# Analyze button to trigger the detection and humanization process when clicked
if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        words = word_count(text)

        if words > max_input_words:
            st.error(f"Text exceeds {max_input_words} word limit.")
        else:
            # Detection of AI-generated content and calculation of scores
            ai_score, human_score = detect_ai(text, detector)

            st.subheader("📊 AI vs Human Score")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("AI Generated (%)", ai_score)

            with col2:
                st.metric("Human Written (%)", human_score)

            # Pie chart visualization of AI vs Human scores for better understanding
            fig = plot_pie(ai_score, human_score)
            st.pyplot(fig)

            # Humanized output section where the original text is rewritten in a more natural and conversational way
            st.subheader("✍️ Humanized Version")

            humanized = humanize_text(
                text,
                tokenizer,
                model,
                max_output_words
            )

            st.write(humanized)

            st.download_button(
                "📥 Download Humanized Text",
                humanized,
                file_name="humanized.txt"
            )