import streamlit as st
from deep_translator import GoogleTranslator

# 1. ??????? ?????? ????????
st.set_page_config(
    page_title="CodeAlpha Translation Tool",
    page_icon="??",
    layout="centered"
)

# 2. ????? ??? Personal Branding ?? ?????? ??????? (Sidebar) - ???? ???????
with st.sidebar:
    st.markdown("### ????? Developer Profile")
    st.markdown("**Yara Hassan**")
    st.markdown("?? *Computer Science Student*")
    st.markdown("---")
    st.markdown("?? **Internship Project**")
    st.markdown("This tool was developed as **Task 1** during the Artificial Intelligence Internship at **CodeAlpha**.")

# 3. ????? ??????? ????????
st.title("?? AI Language Translation Tool")
st.markdown("Welcome! Enter your text below, select the target language, and get your translation instantly.")
st.markdown("---")

# 4. ?????? ?????? ????????
languages_dict = {
    'Arabic': 'ar',
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Italian': 'it',
    'Turkish': 'tr'
}

# 5. ?????? ???????? ?????? ??????
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From (Source Language):", ["Auto Detect"] + list(languages_dict.keys()))

with col2:
    target_lang = st.selectbox("To (Target Language):", list(languages_dict.keys()), index=1)

# 6. ????? ????? ????
text_to_translate = st.text_area("Enter text to translate:", placeholder="Type your text here...", height=150)

# 7. ?? ????? ???????
if st.button("Translate Text", type="primary"):
    if text_to_translate.strip() == "":
        st.warning("?? Please enter some text to translate.")
    else:
        with st.spinner("Translating... Please wait..."):
            try:
                if source_lang == "Auto Detect":
                    translator = GoogleTranslator(source='auto', target=languages_dict[target_lang])
                else:
                    translator = GoogleTranslator(source=languages_dict[source_lang], target=languages_dict[target_lang])
                
                translated_result = translator.translate(text_to_translate)
                
                st.success("? Translation Completed!")
                st.text_area("Translated Output:", value=translated_result, height=150, disabled=False)
                
            except Exception as e:
                st.error(f"An error occurred during translation: {str(e)}")

# 8. ??? Personal Branding ?????? (Footer) - ???? ???????
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 14px;">
        Designed & Developed by <b>Yara Hassan</b> <br>
        AI Internship Portfolio Project @ <b>CodeAlpha</b>
    </div>
    """, 
    unsafe_allow_html=True
)