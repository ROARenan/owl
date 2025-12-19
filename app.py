import streamlit as st
from transformers import pipeline
import torch
import librosa
from typing import Dict, Any, List, Union

# Function to transcribe audio using Whisper model
def transcrever_audio(audio_file):
    # Load Whisper model
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-tiny", device=device)
    
    # Load audio file with librosa
    audio_input, _ = librosa.load(audio_file, sr=16000)

    # Transcribe audio
    result: Union[Dict[str, Any], List[Dict[str, Any]]] = pipe(audio_input, return_timestamps=True)
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
    Upload an audio file in .wav or .mp3 format, and the Whisper model will transcribe it to text.
    You can then download the text file with the transcription.
    """)
    
    # Audio file upload
    audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

    # When user uploads audio
    if audio_file is not None:
        st.audio(audio_file, format="audio/wav")
        
        # Perform transcription
        with st.spinner("Transcribing audio..."):
            transcricao = transcrever_audio(audio_file)
        
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
