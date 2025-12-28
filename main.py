from transformers import pipeline
import torch
from typing import Dict, Any, List, Union

# Certifique-se de que você tem uma GPU compatível com CUDA, ou use a versão CPU se não tiver.
# Se estiver usando a CPU, o código funcionará, mas será mais lento.
device = 0 if torch.cuda.is_available() else -1  # Se você tiver uma GPU, o modelo rodará nela.

# Carregar o modelo Whisper (por exemplo, 'whisper-tiny' ou outro como 'whisper-base', 'whisper-large')
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-tiny", device=device)

# Caminho para o arquivo de áudio local
audio_file_path = "audio_test.wav"  # Altere para o caminho do seu arquivo de áudio

# Use o pipeline para transcrever o áudio
result: Union[Dict[str, Any], List[Dict[str, Any]]] = pipe(audio_file_path, return_timestamps=True)

# Exibir o resultado da transcrição
if isinstance(result, list):
    print("Transcrição:", result[0]["text"])
else:
    print("Transcrição:", result["text"])
