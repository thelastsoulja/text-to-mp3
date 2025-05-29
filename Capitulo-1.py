from gtts import gTTS
from docx import Document

# Carga el documento Word
doc = Document("_____.docx")

# Extrae el texto
text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])

# Crea el archivo de audio (voz en ruso)
tts = gTTS(text=text, lang='ru')
tts.save("new_sound.mp3")

print("✅ Файл MP3 успешно создан: new_sound.mp3")
