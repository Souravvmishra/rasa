import streamlit as st
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def main():
    st.title("Speech Recognition App")
    
    with st.sidebar:
        st.header("Settings")
        language = st.selectbox("Select Language", ["en-US", "es-ES"])
    
    with st.form("audio_input_form"):
        st.write("Press the button below and speak something:")
        submit_button = st.form_submit_button("Start Recording")

    if submit_button:
        with sr.Microphone() as source:
            st.info("Recording...")
            audio = recognizer.listen(source)
            st.success("Recording complete!")

            try:
                with st.spinner("Recognizing..."):
                    text = recognizer.recognize_google(audio, language=language)
                st.info("Recognition complete!")
                st.write(f"You said: {text}")
            except sr.UnknownValueError:
                st.error("Could not understand audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
