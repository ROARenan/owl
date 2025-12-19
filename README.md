# 🦉 OWL

**Optimized Whisper Listener**

OWL is a **self-hosted, privacy-focused audio transcription system** that converts speech into text using an open-source AI model. It is designed to run entirely within your own infrastructure on **AWS**, ensuring that **audio data never leaves your environment**.

The project provides a **minimal web interface** for uploading audio files and receiving accurate transcriptions, making it suitable for internal tools, privacy-sensitive environments, and personal use.

---

## ✨ Features

* 🔐 **Fully self-hosted** – no third-party APIs or external services
* 🧠 **Open-source speech-to-text model** (e.g. Whisper)
* 🦉 **Simple and lightweight UI**
* ⚡ **Fast and accurate transcription**
* ☁️ **AWS-ready architecture**
* 🧩 **Container-friendly (Docker)**
* 🛡️ **Privacy by design** (optional automatic file deletion)

---

## 🏗️ Architecture Overview

```
User
  ↓
Web Interface (HTML / JS)
  ↓
Backend API (FastAPI)
  ↓
Speech-to-Text Engine (Whisper)
```

All components are deployed inside AWS and can run on a single EC2 instance or be scaled using containers.

---

## 🧠 Transcription Engine

OWL uses an **open-source speech recognition model** deployed locally, such as:

* Whisper (OpenAI – open source)
* faster-whisper (recommended for performance)

The model runs entirely on your infrastructure and supports multiple languages, including **English and Portuguese (PT-BR)**.

---

## 🖥️ User Interface

The interface is intentionally minimal:

* Audio file upload
* “Transcribe” button
* Text output area

This keeps the system fast, accessible, and easy to maintain.

---

## 🚀 Getting Started

### Prerequisites

* AWS account
* EC2 instance (CPU or GPU)
* Docker & Docker Compose
* Python 3.10+

---

### Installation (Docker)

```bash
git clone https://github.com/your-org/owl.git
cd owl
docker compose up -d
```

The application will be available at:

```
http://localhost:8000
```

---

## ⚙️ Configuration

Environment variables (example):

```env
MODEL_SIZE=base
LANGUAGE=auto
DELETE_AUDIO_AFTER_PROCESSING=true
```

---

## 🔒 Security & Privacy

OWL is designed for privacy-sensitive use cases:

* Audio files can be processed **in memory only**
* Optional automatic deletion after transcription
* Encrypted storage (EBS)
* IAM-based access control
* HTTPS support

No data is shared with external providers.

---

## 📈 Scaling

OWL can scale from a single-user tool to an internal enterprise service:

* EC2 (single instance)
* ECS / Docker Swarm
* GPU acceleration (g4dn instances)
* Load balancer + autoscaling

---

## 🎯 Use Cases

* Internal company transcription tools
* Legal, medical, or research environments
* Meeting and interview transcription
* Privacy-first AI applications

---

## 🛣️ Roadmap

* [ ] Authentication and user management
* [ ] Batch audio processing
* [ ] Speaker diarization
* [ ] Real-time streaming transcription
* [ ] Webhook and API integrations

---

## 🤝 Contributing

Contributions are welcome!
Please open an issue or submit a pull request.

---

## 📄 License

This project is released under the **MIT License**.