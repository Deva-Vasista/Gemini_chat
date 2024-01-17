import streamlit as st
import google.generativeai as genai
import PIL.Image

st.set_page_config(
    page_title="I see all",
    page_icon="👁️"
)

genai.configure(api_key="AIzaSyA2TETJplezIuU-6VSOgmEPemhCA04GN1A")
model = genai.GenerativeModel("gemini-pro-vision")

prompt = st.text_area("Input your prompt")
file = st.file_uploader("Input the image")

if file and prompt:

    try:
        img = PIL.Image.open(file)

        response = model.generate_content([prompt,img])

        st.code(response.text)
    except:
        print(NameError)
else:
    st.text("please give input and prompt")