from gtts import gTTS
from playsound import playsound

audio = gTTS(text="SABKA cutega,YAAD RAKHNA",lang= "en",slow=False)
audio.save("audio.mp3")
playsound("audio.mp3")