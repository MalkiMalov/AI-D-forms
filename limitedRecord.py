import sounddevice as sd
from scipy.io.wavfile import write
from speechRecognition import recognition

#the function enables recording, transfers the record to WAV file, and then by recognition function converts the WAV file to text file
def rec():
	fs = 44100  # Sample rate
	seconds = 10  # Duration of recording

	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2,dtype='int16')
	print("start")
	sd.wait()  # Wait until recording is finished
	write('output.wav', fs, myrecording)  # Save as WAV file

	text=recognition('output.wav') #uses the recognition function from SpeechRecognition.py to convert the WAV file to text
	f=open("text.txt","w")
	try:
		f.write(text) #write the text to file
	except:
		print(1) #an error occured
	f.close()



