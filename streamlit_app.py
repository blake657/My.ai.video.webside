import streamlit as st
import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
import os

st.title("Pz AI Video Tools")
st.write("ဗီဒီယိုတင်ပါ - မြန်မာအသံနဲ့ စာတန်းထိုး ပြုလုပ်ပေးပါမည်။")

password = st.sidebar.text_input("Password", type="password")

if password == "pz123": 
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.info("AI Processing... Please wait.")

        model = whisper.load_model("base")
        result = model.transcribe("temp_video.mp4")
        
        tts = gTTS(text=result['text'], lang='my')
        tts.save("temp_audio.mp3")

        video = VideoFileClip("temp_video.mp4")
        new_audio = AudioFileClip("temp_audio.mp3")
        final_video = video.set_audio(new_audio)
        
        final_video.write_videofile("output.mp4", codec="libx264")

        st.video("output.mp4")
        with open("output.mp4", "rb") as file:
            st.download_button("Download Video", data=file, file_name="pz_ai_video.mp4")
else:
    st.warning("Please enter password to use the app.")
