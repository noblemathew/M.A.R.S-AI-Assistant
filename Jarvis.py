import webbrowser                      # For web crawling
import requests                        # For Handling Requests
from bs4 import BeautifulSoup          # Html parser
import pyaudio as py                   # Play and record audio
import speech_recognition as sr        # For speech recognition
import random                          # For randomising elements in the array
import pyttsx3                         # text-to-speech conversion
import datetime                        # Reading date and time


# ------------Funtions to Speak-----------------------------------------------------------------------------------------

def SpeakText(command):

   engine = pyttsx3.init()          #initializing pyttsx
   engine.say(command)              #listening for audio
   engine.runAndWait()
   
# ------------Funtions to Search keyword in the Internet-----------------------------------------------------------------------------------------

def Search():
   SpeakText("Say the Keyword...")
   with sr.Microphone() as source:
      audio = r.listen(source)
      vim = r.recognize_google(audio)
      webbrowser.open_new_tab("https://www.google.com/search?q=" + vim)   #Opens the browser
      return

# ------------Funtions to webcrawl news headlines from BBC News-----------------------------------------------------------------------------------------
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
first = ["Hello Sir", "Welcome Sir","Welcome back Sir", "Good to See You Sir","Bonjour Sir","Hi there Sir","hola Sir","guten tag sir","salve sir","anyoung haseyo"] # Welcome Dataset Array
intro=["Hello","Hey","Hai","Hi","what's up","Whatsup","you up","wake up"]     # Greet Dataset Array
name=["Jarvis!","Don't you forget!, Your Assistant Jarvis","Its me Sir, Jarvis","Your Personal Assistant Jarvis","Hola, I am Jarvis","I am Jarvis, your assistant"] # Jarvis name Dataset Array
url='https://www.bbc.com/news'  #BBC News link
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')  #Reading the html body and finding all h3 tags
headlines = soup.find('body').find_all('h3')
r=sr.Recognizer()

#------------------------------------------Finding the Keyword from the User-----------------------------------------------------------------------
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

#----------------------------------------------Error in case of Listening-------------------------------------------------------------------------
   except(Exception):
      print(" ")
