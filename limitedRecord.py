import sounddevice as sd
from scipy.io.wavfile import write
from speechRecognition import recognition

def rec():
	fs = 44100  # Sample rate
	seconds = 10  # Duration of recording

	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2,dtype='int16')
	print("start")
	sd.wait()  # Wait until recording is finished
	write('output.wav', fs, myrecording)  # Save as WAV file

	text=recognition('output.wav')
	f=open("text.txt","w")
	try:
		f.write(text)
	except:
		print(1)
	f.close()



