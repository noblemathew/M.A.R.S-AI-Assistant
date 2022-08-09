import pyaudio as py
import speech_recognition as sr
r=sr.Recognizer()
while(1):
   try:
      with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source, duration=0.2)
         audio=r.listen(source)
         var = r.recognize_google(audio)
         print(var)
   except(Exception):
      print("Could not catch that. Can you say that again?")

