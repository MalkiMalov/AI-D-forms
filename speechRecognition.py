#SpeechRecognition
import speech_recognition as sr

#The function receives a WAV file, and convert it to text using Speech Recognition
def recognition(file):
    r = sr.Recognizer() #Create a Recognizer object
    audiofile = sr.AudioFile(file) #Convert the WAV file to AudioFile
    with audiofile as source:
        clip = r.record(source) #Convert the AudioFile file to DataFile using record function
    s = r.recognize_google(clip, language="he-IL") #Convert the DataFile to text using the recognize_google function
    f = open("text_from_speech.txt", "w")
    f.write(str(s)) #Write the text to file
    return
