#SpeechRecognition
import speech_recognition as sr
def recognition(file):
    r = sr.Recognizer()
    audiofile = sr.AudioFile(file)
    with audiofile as source:
        clip = r.record(source)
    s = r.recognize_google(clip, language="he-IL")
    f = open("out.txt", "w")
    f.write(str(s))
    print(s)
    return
