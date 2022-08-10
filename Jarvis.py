import webbrowser
import requests
from bs4 import BeautifulSoup
import pyaudio as py
import speech_recognition as sr
import random
import pyttsx3
import datetime


# ------------Funtions to Speak-----------------------------------------------------------------------------------------

def SpeakText(command):

   engine = pyttsx3.init()
   engine.say(command)
   engine.runAndWait()

def Search():
   SpeakText("Say the Keyword...")
   with sr.Microphone() as source:
      audio = r.listen(source)
      vim = r.recognize_google(audio)
      webbrowser.open_new_tab("https://www.google.com/search?q=" + vim)
      return

def News():
   SpeakText("Reading News...")
   print("Reading News...")
   for x in headlines:
      print(x.text.strip())
      SpeakText(x.text.strip())
   return

def Date_and_time():
   datetime_object = datetime.datetime.now()
   print(datetime_object.strftime("%B " + "%d " + "%Y " + " %I " + "%M " + " %p"))
   SpeakText(datetime_object.strftime("%B " + "%d " + "%Y " + " %I " + "%M " + " %p"))
   return

#-----------------------------------------------------------------------------------------------------------------------
first = ["Hello Sir", "Welcome Sir","Welcome back Sir", "Good to See You Sir","Bonjour Sir","Hi there Sir","hola Sir","guten tag sir","salve sir","anyoung haseyo"]
intro=["Hello","Hey","Hai","Hi","what's up","Whatsup","you up","wake up"]
name=["Jarvis!","Don't you forget!, Your Assistant Jarvis","Its me Sir, Jarvis","Your Personal Assistant Jarvis","Hola, I am Jarvis","I am Jarvis, your assistant"]
url='https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
r=sr.Recognizer()

while(1):
   try:
      with sr.Microphone() as source:
         print("Listening...")
         audio=r.listen(source)
         var = r.recognize_google(audio)
         print(var)
         if "search" in var:
            Search()
         if "news" in var or "headlines" in var:
            News()
         if "date" in var or "time" in var:
            Date_and_time()
         if "Jarvis" in var:
            for i in intro:
               if(i.casefold() in var):
                  SpeakText(random.choice(first))
         if "your name" in var or "who" in var and "you" in var or "may" in var:
            SpeakText(random.choice(name))





   except(Exception):
      print(" ")
