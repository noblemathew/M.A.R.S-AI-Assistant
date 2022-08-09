import webbrowser

import pyaudio as py
import speech_recognition as sr
import random
import pyttsx3

def SpeakText(command):

   engine = pyttsx3.init()
   engine.say(command)
   engine.runAndWait()

r=sr.Recognizer()
intro=["Hello","Hey","Hi Jarvis","Hey Whatsup","Jarvis you up","Jarvis","Hey Man","Jarvis wake up","Jarvis wake up daddy's home","wake up daddy's home","hello Jarvis"]
first = ["Hello Sir", "Welcome Sir","Welcome back Sir", "Good to See You Sir","Bonjour Sir","Hi there Sir","hola Sir","guten tag sir","salve sir","anyoung haseyo"]
while(1):
   try:
      with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source, duration=0.2)
         audio=r.listen(source)
         var = r.recognize_google(audio)
         print(var)
         for i in intro:
            if(i.casefold()==var.casefold()):
               SpeakText(random.choice(first))
               break
         if(var=="web search"):
            SpeakText("Say Anything")
            with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source, duration=0.2)
               audio = r.listen(source)
               vim = r.recognize_google(audio)
               webbrowser.open_new_tab("https://www.google.com/search?q="+vim)







   except(Exception):
      print(" ")


