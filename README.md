# 🦉 OWL - Optimized Whisper Listener

A simple, self-hosted audio transcription tool using OpenAI's Whisper model. Perfect for transcribing meetings, interviews, and audio recordings locally without sending data to external services.

---

## ✨ What It Does

OWL is a **lightweight Streamlit web application** that:
- Uploads audio files (WAV or MP3)
- Transcribes them using the Whisper AI model
- Displays the transcription in your browser
- Lets you download the result as a text file

**Privacy-focused**: Everything runs on your local machine. No data leaves your computer.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- (Optional) CUDA-compatible GPU for faster processing

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/owl.git
cd owl
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

**Web Interface** (Recommended):
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

**Command Line** (for testing):
```bash
python main.py
```
(Edit `main.py` to point to your audio file)

---

## 📖 How to Use

1. **Open the web interface** (it launches automatically)
2. **Click "Browse files"** to upload an audio file (WAV or MP3)
3. **Wait** while Whisper transcribes (shows a spinner)
4. **Read the transcription** displayed on screen
5. **Click "Download transcription as .txt"** to save the result

---

## 🎯 Current Features

| Feature | Status | Notes |
|---------|--------|-------|
| Web interface | ✅ Working | Streamlit-based |
| Audio upload | ✅ Working | WAV and MP3 only |
| Whisper transcription | ✅ Working | Using whisper-tiny model |
| Portuguese language | ✅ Working | Hardcoded in `app.py` |
| Text download | ✅ Working | Saves as .txt file |
| GPU acceleration | ✅ Working | Auto-detects CUDA |
| Local processing | ✅ Working | No external API calls |

---

## 🧠 Technical Details

### Model
- **Whisper-tiny** from OpenAI (open source)
- Loaded via Hugging Face Transformers
- Runs locally on CPU or GPU
- Currently configured for Portuguese language

### Audio Processing
- Uses `librosa` to load audio files
- Resamples to 16kHz (Whisper requirement)
- Supports WAV and MP3 formats

### Dependencies
Key packages:
- `streamlit` - Web interface
- `transformers` - Whisper model
- `torch` - PyTorch for model inference
- `librosa` - Audio file processing

See `requirements.txt` for complete list.

---

## ⚙️ Configuration

### Change Language

Edit `app.py`, line 14:
```python
# Change "portuguese" to "english", "spanish", etc.
result = pipe(audio_input, return_timestamps=True, generate_kwargs={"language": "portuguese"})
```

### Use Different Whisper Model

Edit `app.py`, line 10:
```python
# Options: whisper-tiny, whisper-base, whisper-small, whisper-medium, whisper-large
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=device)
```

**Note**: Larger models are more accurate but slower and require more memory.

---

## 📊 Performance

| Model | Speed | Accuracy | Memory |
|-------|-------|----------|--------|
| whisper-tiny | Fast | Good | ~1 GB |
| whisper-base | Medium | Better | ~1.5 GB |
| whisper-small | Slow | Great | ~2.5 GB |

**Current**: Using `whisper-tiny` for speed.

---

## 🔒 Privacy & Security

- ✅ **100% local processing** - No external API calls
- ✅ **No data collection** - Nothing is sent anywhere
- ✅ **Open source model** - Whisper is publicly available
- ✅ **Self-hosted** - You control everything

**Note**: This is a personal tool. For production use in enterprise environments, additional security measures would be needed (authentication, encryption, audit logging, etc.).

---

## 🛠️ Troubleshooting

### "CUDA out of memory"
- Use a smaller model (whisper-tiny)
- Or force CPU mode by editing `app.py`:
```python
device = -1  # Force CPU
```

### "File format not supported"
- Only WAV and MP3 are currently supported
- Convert your audio file using ffmpeg:
```bash
ffmpeg -i input.m4a output.mp3
```

### Slow transcription
- Use GPU if available (10x faster)
- Or use a smaller model (whisper-tiny)

---

## 🛣️ Roadmap

### Current Version (v0.1)
- [x] Basic Streamlit interface
- [x] Whisper model integration
- [x] Portuguese language support
- [x] WAV/MP3 file upload
- [x] Text download

### Future Ideas
- [ ] Support more audio formats (M4A, OGG, FLAC)
- [ ] Multi-language auto-detection
- [ ] Batch processing (multiple files)
- [ ] Speaker diarization (who said what)
- [ ] Timestamps in output
- [ ] Docker container for easy deployment
- [ ] AWS deployment option (for teams)

---

## 🤝 Contributing

This is a personal project, but contributions are welcome!

**Ideas for contributions**:
- Add support for more audio formats
- Improve the UI/UX
- Add language auto-detection
- Create Docker container
- Add tests

---

## 📄 License

This project is released under the **MIT License** - feel free to use it however you want!

---

## 🙏 Acknowledgments

- **OpenAI** for the Whisper model
- **Hugging Face** for the Transformers library
- **Streamlit** for the easy web framework

---

## 📧 Contact

Questions or suggestions? Feel free to open an issue or reach out!

---

**Note**: This is a personal tool I created for my own use and am sharing with Amazon employees who might find it helpful. It's not an official Amazon project and doesn't have enterprise features like SSO, audit logging, or AWS integration. For production use, additional development would be needed.
