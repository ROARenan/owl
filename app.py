import os
import tempfile

import streamlit as st
from transformers import pipeline
import torch
import librosa
from moviepy import VideoFileClip
from typing import Dict, Any, List, Union

VIDEO_EXTENSIONS = {"mp4"}


def extrair_audio_de_video(video_path: str) -> str:
    """Extract the audio track from a video file into a temporary WAV file."""
    audio_fd, audio_path = tempfile.mkstemp(suffix=".wav")
    os.close(audio_fd)

    with VideoFileClip(video_path) as clip:
        if clip.audio is None:
            raise ValueError("The uploaded video has no audio track.")
        clip.audio.write_audiofile(audio_path, logger=None)

    return audio_path


# Function to transcribe audio using Whisper model
def transcrever_audio(audio_file):
    # Load Whisper model
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-tiny", device=device)
    
    # Load audio file with librosa
    audio_input, _ = librosa.load(audio_file, sr=16000)

    # Transcribe audio
    result: Union[Dict[str, Any], List[Dict[str, Any]]] = pipe(audio_input, return_timestamps=True, generate_kwargs={"language": "portuguese"})
    if isinstance(result, list):
        return result[0]["text"]
    return result["text"]

# Streamlit interface
def app():
    # Page configuration
    st.set_page_config(page_title="OWL - Optimized Whisper Listener", page_icon="🦉")
    
    # Title
    st.title("🦉 OWL - Optimized Whisper Listener")
    
    # Description
    st.write("""
    Upload an audio file (.wav or .mp3) or a video file (.mp4), and the Whisper model will transcribe it to text.
    You can then download the text file with the transcription.
    """)
    
    # Audio/video file upload
    uploaded_file = st.file_uploader("Upload audio or video file", type=["wav", "mp3", "mp4"])

    # When user uploads a file
    if uploaded_file is not None:
        file_extension = uploaded_file.name.rsplit(".", 1)[-1].lower()
        is_video = file_extension in VIDEO_EXTENSIONS
        temp_audio_path = None

        if is_video:
            st.video(uploaded_file)

            # Save the uploaded video to a temp file so moviepy can read it
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as temp_video:
                temp_video.write(uploaded_file.getbuffer())
                temp_video_path = temp_video.name

            try:
                with st.spinner("Extracting audio from video..."):
                    temp_audio_path = extrair_audio_de_video(temp_video_path)
                audio_source = temp_audio_path
            finally:
                os.remove(temp_video_path)
        else:
            st.audio(uploaded_file, format="audio/wav")
            audio_source = uploaded_file

        # Perform transcription
        try:
            with st.spinner("Transcribing audio..."):
                transcricao = transcrever_audio(audio_source)
        finally:
            if temp_audio_path is not None:
                os.remove(temp_audio_path)
        
        # Display transcription
        st.subheader("Audio transcription:")
        st.write(transcricao)
        
        # Generate .txt file for download
        st.subheader("Download Transcription")
        with open("transcription.txt", "w") as f:
            f.write(transcricao)
        
        st.download_button(
            label="Download transcription as .txt",
            data=open("transcription.txt", "rb"),
            file_name="transcription.txt",
            mime="text/plain"
        )

# Run Streamlit app
if __name__ == "__main__":
    app()
