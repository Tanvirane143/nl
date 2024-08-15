b. Convert the given text to speech
Steps:
1. create file.txt in respective folder.
2. Enter some message in file.txt.
3. Save texttospeech.py file at same location.

code:
from gtts import gTTS
import os
f = open('1.txt')
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge)
audio.save("wishes.wav")
os.system("wishes.wav")
print("program executed succesfully.")
