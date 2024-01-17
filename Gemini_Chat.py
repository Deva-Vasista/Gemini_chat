import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Chat with Gemini",
    page_icon="🤖"
)
with st.sidebar:
    st.subheader("Parameters")

def_key = "AIzaSyA2TETJplezIuU-6VSOgmEPemhCA04GN1A"
default = st.sidebar.button("Use Default")

Gemini_Key = def_key

if "Key" not in st.session_state:
    st.session_state["Key"]  = Gemini_Key
        

    
st.title("🔎 Gemini Chat- Chat with search")
genai.configure(api_key=Gemini_Key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not Gemini_Key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()

    model =genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat.send_message(prompt,stream=True)
            response.resolve()
            st.session_state.messages.append({"role": "assistant", "content": response.text}) 
            for chunk in response:
                st.markdown(chunk.text)
