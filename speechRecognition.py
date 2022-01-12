#SpeechRecognition
import speech_recognition as sr

#the function receives a WAV file, and convert it to text using Speech Recognition
def recognition(file):
    r = sr.Recognizer() #create a Recognizer object
    audiofile = sr.AudioFile(file) #convert the WAV file to AudioFile
    with audiofile as source:
        clip = r.record(source) #convert the AudioFile file to DataFile using record function
    s = r.recognize_google(clip, language="he-IL") #convert the DataFile to text using the recognize_google function
    f = open("text_from_speech.txt", "w")
    f.write(str(s)) #write the text to file
    print(s)
    return
