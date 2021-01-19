from gtts import gTTS
from playsound import playsound
from datetime import datetime

# audio = gTTS(text="tujhi aai ghaall",lang="mr",slow=False)
# audio.save("audio.mp3")
# playsound("audio.mp3")


def add_timestamp_filename(filename):
    filename = filename.split(".")
    file = filename[0]
    file_ext = filename[1]
    now = datetime.now();
    timestamp = str(now.timestamp());
    timestamp = timestamp.replace(".", "")
    filename = file + timestamp + "." + file_ext

    return filename


