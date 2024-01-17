import streamlit as st 
import google.generativeai as genai
from streamlit_ace import st_ace
st.set_page_config("Translator")
st.title("Translate your Code")

with st.sidebar:
    if "Key" not in st.session_state:
        Gemini_Key = st.text_input("Gemini", key="Gemini_key", type="password")
        st.session_state["Key"]  = Gemini_Key
    else:
        st.success("Gemini Key is provided")

model = genai.GenerativeModel("gemini-pro")

# Create a function to translate text from one programming language to another
def translate_code(t, source_language, target_language):
  """Translates text from one programming language to another.

  Args:
    text: The text to be translated.
    source_language: The programming language of the source text.
    target_language: The programming language of the target text.

  Returns:
    The translated text.
  """
  source_language = source_language.lower()
  target_language = target_language.lower()

  # Translate the text
  prompt = f"Translate {t} from {source_language} to {target_language}"
  response = model.generate_content(prompt)

  return response.text

# Create a Streamlit app
st.title("Gemini Translate")
l,r = st.columns(2)
# Create a form to collect the user's input
with l.form("translate_form"):
  # Create a text area for the user to input their code
  # Create a dropdown menu for the user to select the source language
  source_language = st.selectbox(
      "Select the source language:",
      ["python", "javascript", "java", "c++", "c#"],
      index=0,
  )
  
  text = st_ace(placeholder="Source Code",language=source_language)
  target_language = st.selectbox(
      "Select the target language:",
      ["python", "javascript", "java", "c++", "c#"],
      index=1,
  )

  submitted = st.form_submit_button("Translate")

if submitted:
  translated_text = translate_code(text, source_language, target_language)
  
  r.code(translated_text,language=target_language)
  
  r.success("Done")