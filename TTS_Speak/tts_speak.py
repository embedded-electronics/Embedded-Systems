"""
Text-to-Speech Script (tts_speak.py)
-----------------------------------------

Standard Run Process:
1. Create a virtual environment (only once):
      python3 -m venv venv

2. Activate the virtual environment:
      source venv/bin/activate

3. Install dependencies (auto-install will also work):
      pip install gtts

4. Run the script:
      python3 tts_speak.py

This script:
- Converts input text to speech using gTTS
- Supports English, Hindi, Bengali
- Saves MP3 files in Windows Downloads folder (/mnt/c/Users/dibye/Downloads)
"""
from gtts import gTTS
import os
import getpass
from datetime import datetime

# Input from user
text = input("Enter text to convert to speech: ")

# Choose language
print("Choose language: [1] English [2] Hindi [3] Bengali")
lang_choice = input("Your choice (1/2/3): ")

lang_map = {'1': 'en', '2': 'hi', '3': 'bn'}
lang = lang_map.get(lang_choice, 'en')  # Default to English

# Generate speech
tts = gTTS(text=text, lang=lang, tld='co.in')

# Create timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"output_{timestamp}.mp3"
tts.save(filename)

# Define download path for current Windows user
windows_user = getpass.getuser()
download_path = f"/mnt/c/Users/dibye/Downloads/{filename}"

# Move file
os.system(f"cp {filename} '{download_path}'")

print(f"✅ Voice saved to your Downloads folder as {filename}")
