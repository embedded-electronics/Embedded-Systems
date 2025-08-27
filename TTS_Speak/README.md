root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# source venv/bin/activate
(venv) root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# 

(venv) root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# pip install gtts
Collecting gtts
  Using cached gTTS-2.5.4-py3-none-any.whl.metadata (4.1 kB)
Collecting requests<3,>=2.27 (from gtts)
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting click<8.2,>=7.1 (from gtts)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->gtts)
  Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.27->gtts)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.27->gtts)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.27->gtts)
  Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Using cached gTTS-2.5.4-py3-none-any.whl (29 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.7/64.7 kB 942.9 kB/s eta 0:00:00
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 161.2/161.2 kB 2.5 MB/s eta 0:00:00
Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (151 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.8/151.8 kB 2.7 MB/s eta 0:00:00
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Installing collected packages: urllib3, idna, click, charset_normalizer, certifi, requests, gtts
Successfully installed certifi-2025.8.3 charset_normalizer-3.4.3 click-8.1.8 gtts-2.5.4 idna-3.10 requests-2.32.5 urllib3-2.5.0
(venv) root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# 

(venv) root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# python3 tts_speak.py 
Enter text to convert to speech: Hello Shilpa! How are you?
Choose language: [1] English [2] Hindi [3] Bengali
Your choice (1/2/3): 1
✅ Voice saved to your Downloads folder as output_2025-08-27_06-43-03.mp3
(venv) root@DESKTOP-T6I6DAE:/home/dibyendu/TTS_Speak# 
