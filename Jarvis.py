import webbrowser                      # For web crawling
import requests                        # For Handling Requests
from bs4 import BeautifulSoup          # Html parser
import pyaudio as py                   # Play and record audio
import speech_recognition as sr        # For speech recognition
import random                          # For randomising elements in the array
import pyttsx3                         # text-to-speech conversion
import datetime                        # Reading date and time
import os
from google import genai

   
# ------------Funtions to Search keyword in the Internet-----------------------------------------------------------------------------------------

def Search():
   SpeakText("Say the Keyword...")
   with sr.Microphone() as source:
      audio = r.listen(source)
      vim = r.recognize_google(audio)
      webbrowser.open_new_tab("https://www.google.com/search?q=" + vim)   #Opens the browser
      return

# ------------Funtions to webcrawl news headlines from BBC News-----------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import time

def SpeakText(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set Heera voice silently
    for voice in voices:
        if "David" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 190)
    engine.setProperty('volume', 0.5)
    engine.say(text)
    engine.runAndWait()
SpeakText("Hello, My name is Jarvis!")





def News():
    url = 'https://timesofindia.indiatimes.com/briefs'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    print("HTTP Status Code:", response.status_code)
    
    if response.status_code != 200:
        SpeakText("Sorry, I couldn't fetch the news.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    boxes = soup.find_all('div', class_='brief_box')

    print("News boxes found:", len(boxes))
    
    if not boxes:
        SpeakText("No news headlines found.")
        return

    SpeakText("Here are today's top news stories.")
    r = sr.Recognizer()

    for count, box in enumerate(boxes[:10], start=1):  # Max 10 for safety
        h2 = box.find('h2')
        para = box.find('p')

        headline = h2.text.strip() if h2 else "No headline"
        summary = para.text.strip() if para else "No summary"

        print(f"\nHeadline {count}: {headline}")
        print(f"Summary: {summary}\n")

        SpeakText(f"Headline {count}: {headline}")
        SpeakText(summary)
        time.sleep(2)

        # After every 3 headlines, ask to continue
        if count % 3 == 0 and count != len(boxes[:10]):
            SpeakText("Do you want me to continue?")
            print("Listening for yes/no...")
            try:
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=5)
                    reply = r.recognize_google(audio).lower()
                    print(f"User said: {reply}")
                    if "no" in reply:
                        SpeakText("Okay, stopping the news.")
                        return
            except:
                SpeakText("I didn't catch that. Stopping the news.")
                return

    SpeakText("That's all for now.")

def Date_and_time():
   datetime_object = datetime.datetime.now()
   print(datetime_object.strftime("%B " + "%d " + "%Y " + " %I " + "%M " + " %p"))
   SpeakText(datetime_object.strftime("%B " + "%d " + "%Y " + " %I " + "%M " + " %p"))
   return
def shutdown_procedure():
   SpeakText("Are you sure you want to shut down the system? Please say yes or no.")
   try:
               with sr.Microphone() as source:
                     confirm_audio = r.listen(source, timeout=5)
                     confirm = r.recognize_google(confirm_audio).lower()
                     print("Confirmation:", confirm)
                     
                     if "yes" in confirm:
                        SpeakText("Shutting down your system, Sir. Countdown begins.")
                        for i in range(10, 0, -1):
                           SpeakText(str(i))
                           time.sleep(1)
                        os.system("shutdown /s /t 1")  # Shutdown command only once
                     else:
                        SpeakText("Shutdown cancelled.")
   except Exception as e:
               print("Error during confirmation:", e)
               SpeakText("I didn't hear your confirmation. Cancelling shutdown.")

def sleep_procedure():
    SpeakText("Are you sure you want to put the system to sleep? Please say yes or no.")
    try:
               with sr.Microphone() as source:
                     confirm_audio = r.listen(source, timeout=5)
                     confirm = r.recognize_google(confirm_audio).lower()
                     print("Confirmation:", confirm)
                     if "yes" in confirm:
                        SpeakText("Putting your system to sleep. Countdown begins.")
                        for i in range(5, 0, -1):
                           SpeakText(str(i))
                           time.sleep(1)
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                     else:
                        SpeakText("Sleep cancelled.")
    except Exception as e:
               print("Error during confirmation:", e)
               SpeakText("I didn't hear your confirmation. Cancelling sleep.")

def Chats(prompt):
    try:
        print("", prompt)
        responses = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": f"You are Jarvis, a helpful assistant. {prompt}"}
                    ]
                }
            ]
        )
        reply = responses.text.strip().replace("*", "")  # Remove asterisks
        print(reply)
        return reply
    except Exception as e:
        print("Gemini ERROR:", e)
        return "Sorry, something went wrong with Gemini."



#-----------------------------------------------------------------------------------------------------------------------
first = ["Hello Sir", "Welcome Sir","Welcome back Sir", "Good to See You Sir","Bonjour Sir","Hi there Sir","hola Sir","guten tag sir","salve sir","anyoung haseyo"] # Welcome Dataset Array
intro=["hello","hey","hai","hi","what's up","whatsup","you up","wake up"]     # Greet Dataset Array
name=["Jarvis!","Don't you forget!, Your Assistant Jarvis","Its me Sir, Jarvis","Your Personal Assistant Jarvis","Hola, I am Jarvis","I am Jarvis, your assistant"] # Jarvis name Dataset Array
url='https://www.bbc.com/news'  #BBC News link
client = genai.Client(api_key="AIzaSyA4XRtPATIqys5Ct2AXqKpWfN-0D217Dzo")
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
         elif "news" in var or "headlines" in var:
            News()
         elif "date" in var or "time" in var:
            Date_and_time()
         elif var in intro:
            SpeakText(random.choice(first))
      
         elif "your name" in var or ("who" in var and "you" in var) or "may" in var:
            SpeakText(random.choice(name))
         elif "exit" in var or "stop" in var or "close" in var:
             break
         elif "power off" in var or "shutdown" in var:
            shutdown_procedure()
         elif "sleep" in var:
            sleep_procedure()
         else:
            audio=r.listen(source)
            var = r.recognize_google(audio)
            SpeakText(Chats(var))

            

#----------------------------------------------Error in case of Listening-------------------------------------------------------------------------
   except(Exception):
      print(Exception)
