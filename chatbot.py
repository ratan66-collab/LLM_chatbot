import os
import streamlit as st
from dotenv import load_dotenv
import google.genertiveai as genai

# import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyAcY6ou4oYlX9xRg7coCboTVP74zP3k2Ec"
genai.configure(api_key="AIzaSyAcY6ou4oYlX9xRg7coCboTVP74zP3k2Ec")
genai.configure(api_key=os. environ["GOOGLE_API_KEY"])

model  = genai.GenerativeModel("gemini-pro")

# load environment variables
load_dotenv()

#configure streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  #favicon emoji
    layout="centered",    #page layout option
)

GOOGLE_API_KEY =
os.getenv("AIzaSyDyWBGLbtDBKpInw_NsMaC9gVDdOzoIYp4")


# ste up google Gemini-AI Model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


# Function to translate roles between Gemini-Pro and streamlit terminology

def translate_role_streamlit(user_role):
    if user_role =="model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])



# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")


# Display the chat history
for message in st.session_state.chat_session.history:
    with
st.chat_message(translate_role_for_streamlit(message.role)):
             st.markdown(message.parts[0].text)

# input field for user's message
if user_prompt:
    #Add user's message to chat and display it
     st.chat_message("user".markdown(user_prompt))


    # send user's message to Gemini-Pro and get the response
     gemini_response =
st.session_state.chat_session.send_message(user_prompt)

     # display Gemini-Pro's response'
     with st.chat_message("assistant"):
         st.markdown(gemini_response.text)

