import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text instantly between multiple languages using Google Translator.")
text = st.text_area("Enter text")

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)
        st.success("Translation")
        st.write(translated)
    else:
        st.warning("Please enter some text.")
