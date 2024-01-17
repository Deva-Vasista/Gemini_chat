import streamlit as st
from streamlit_mermaid import st_mermaid
import google.generativeai as genai
from PIL import Image
from streamlit.components.v1 import html
import base64

def download_image(code):
    image_data = mermaid_chart(code)

    # Convert HTML to image
    image = st.image(image_data, use_container_width=True, format="PNG")

    # Create download link
    image_encoded = base64.b64encode(image.data).decode()
    href = f'<a href="data:file/png;base64,{image_encoded}" download="mermaid_chart.png">Download Chart</a>'
    
    st.markdown(href, unsafe_allow_html=True)

def mermaid_chart(code):
    html_code = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <div class="mermaid">{code}</div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{startOnLoad:true}});</script>
    """
    return html_code


st.set_page_config(
    page_title="Mermaid",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    if "Key" not in st.session_state:
        Gemini_Key = st.text_input("Gemini", key="Gemini_key", type="password")
        st.session_state["Key"]  = Gemini_Key
    else:
        st.success("Gemini Key is provided")

model = genai.GenerativeModel("gemini-pro")

st.title("Streamlit Mermaid ")



Prompt = st.text_input("Prompt")

response = model.generate_content(f"{Prompt} give me pure mermaid script code")




generate = st.button("generate")
if generate:
    
    code = st.text_area("Mermaid Code", response.text[10:-3])
    
    html(mermaid_chart(code), width=1500, height=1500)