#importing all the required libraries
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import pyautogui

#setting up engine that would be converting text-to-speech
engine=pyttsx3.init()
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

def speakAndPrint(a,rateToSet=145):
    engine.setProperty('rate', rateToSet)
    engine.say(a)
    engine.runAndWait()
    print(a)

def songToPlay():
    r=sr.Recognizer()
    mic=sr.Microphone()
    speakAndPrint("Speak The Choice of Your Song")
    while(True):
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source,timeout=5)
            trans=r.recognize_google(audio)
            speakAndPrint("Did you say "+trans)
            flag=True
            while(flag):
                    try:
                        #Listening for confirming now
                        with mic as source:
                            r.adjust_for_ambient_noise(source)
                            confirmAudio=r.listen(source,timeout=5)
                        confirm=r.recognize_google(confirmAudio)
                        if(confirm.lower()=="yes" or confirm.lower()=="ya" or confirm.lower()=="no" or confirm.lower()=="na"):
                            flag=False
                        else:
                            speakAndPrint("Please say either Yes or No") 
                    except:
                        speakAndPrint("Sorry I Couldn't Get That")
                        speakAndPrint("Please Confirm Your Choice Again")     
            if(confirm.lower()=="yes" or confirm.lower()=="ya"):
                return trans
            speakAndPrint("Repeating The Process As You Said No")
            speakAndPrint("Please Speak The Choice of Your Song Again")           
        except:
            speakAndPrint("What You Said Was Not Clear")
            speakAndPrint("Please Speak The Choice of Your Song Again")

#initial announcement
speakAndPrint("Please Ensure that your Microphone is unmuted and there is less noise around you",210)

#calling function to determine which song to be played
key=songToPlay()

#automating the browser
browser=webdriver.Firefox()
browser.maximize_window()
urlToHit="https://www.youtube.com/results?search_query="+key
browser.get(urlToHit)
pyautogui.moveTo(470,327)
pyautogui.doubleClick()
