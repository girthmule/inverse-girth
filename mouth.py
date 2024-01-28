from gtts import gTTS
import subprocess

def respond(response_text):
    global audio_prcoess
 
    print(response_text)
    s = response_text
    file = "file.mp3"
    tts = gTTS(text=s)
    tts.save(file)
    audio_process = subprocess.Popen(["mpg123", file],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
def shutup():
    global audio_process

    # Check if the process is running and terminate it
    if audio_process is not None and audio_process.poll() is None:
        audio_process.terminate()
        audio_process = None