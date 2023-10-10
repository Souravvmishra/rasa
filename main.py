import streamlit as st
import speech_recognition as sr
import pyttsx3

PAGE_CONFIG = {"page_title": "Conversational Bot",
               "page_icon": "🤖", "layout": "centered"}
st.set_page_config(**PAGE_CONFIG)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://media.istockphoto.com/id/1139397630/vector/abstract-background.jpg?s=612x612&w=0&k=20&c=7BitNm1dVbhMW37_rmqhXHL6odkWMEs0fhBQFgoYFYo=");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id)

rec = sr.Recognizer()

bot_message = ""

st.title("Voice Controlled Bot")

# while True:
with sr.Microphone() as source:
    st.text("Jarvis is Listening...")
    message = rec.listen(source)

try:
    query = rec.recognize_google(message, language="en-in")
    st.text("You Said : {}".format(query))
    for i in range(10):
        st.write('')
    st.text('---------- End of Speech-to-Text ---------')

except Exception as e:
    converter.say(str(e))
    converter.runAndWait()
