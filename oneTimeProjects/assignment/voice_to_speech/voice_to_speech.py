from gtts import gTTS
from threading import Thread
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
text = ""
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(rate=RATE, channels=CHANNELS, format=FORMAT, input=True, frames_per_buffer=CHUNK)

# frames = []

# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save("test.mp3")

def get_word():
	global text
	while(1):
		try:
			with sr.Microphone() as mic:
				r.adjust_for_ambient_noise(mic, duration=0.2)
				audio2 = r.listen(mic)
				MyText = r.recognize_google(audio2)
				text = MyText
				break
		except sr.RequestError as e:
			print("RequestError")
		except sr.UnknownValueError as e:
			print("UnknownValueError")

word_thread = Thread(target=get_word)
word_thread.start()

