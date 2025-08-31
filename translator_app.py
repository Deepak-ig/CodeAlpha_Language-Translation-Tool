import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Translator App")

st.write("Translate any text to multiple languages.")

text_to_translate = st.text_area("Enter text to translate:")
lang = st.selectbox("Select target language:", ["en", "hi", "ta", "fr", "es", "ru"])

if st.button("Translate"):
    if text_to_translate.strip() != "":
        translated_text = GoogleTranslator(source='auto', target=lang).translate(text_to_translate)
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate.")

