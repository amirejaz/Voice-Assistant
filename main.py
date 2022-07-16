from importlib.resources import path
from importlib.util import spec_from_file_location
from tokenize import Special
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import os
import keyboard
import pyjokes
from PyDictionary import PyDictionary as diction 
from googletrans import Translator
import requests
import bs4
from pywikihow import search_wikihow


Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
# print(voices)
Assistant.setProperty("voices",voices[0].id)
Assistant.setProperty("rate",170)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")  
            query = command.recognize_google(audio,language="en-us")
            print(f"You said: {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def TaskExecution():
    Speak("hey Amir")
    Speak("welcome back sir..")
    Speak("How are you?")

    def Music():
        Speak("Tell me the name of song!")
        MusicName = takecommand()

        if "chal ghar chalein" in query:
            os.startfile("C:\\Users\Hunani Trading Co\\Music\\ChalGharChalein.mp3")

        else:
            pywhatkit.playonyt(MusicName)

        Speak("Your song has been started , Enjoy sir!") 

    def Whatsapp():
        Speak("Tell me the name of person!")
        name = takecommand()

        if "duryab" in query:
            Speak("Tell me the message")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("time in hour")
            hour = int(takecommand())
            Speak("time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+923323696360",msg,hour,min,20)
            Speak("Ok sir! , Sending Whatsapp message")

        else: 
            Speak("Tell me the phone number")
            phone = int(takecommand())
            ph = "+92" + phone
            Speak("Tell me the message")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("time in hour")
            hour = int(takecommand())
            Speak("time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Ok sir! , Sending Whatsapp message")    

    def OpenApp():
        Speak("Ok sir! wait a second")

        if "code" in query:
            os.startfile("C:\\Users\\Hunani Trading Co\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe")

        elif "chrome" in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "facebook" in query:
            webbrowser.open("https://wwww.facebook.com/")          

        elif "instagram" in query:
            webbrowser.open("https://wwww.instagram.com/")

        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com/")    

        elif "maps" in query:
            webbrowser.open("https://www.google.com/maps")

        Speak("Done Sir")

    def CloseApp():
        Speak("OK sir wait a second")

        if "youtube" in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif "instagram" in query:
            os.system("TASKKILL /f /im chrome.exe")
        
        elif "facebook" in query:
            os.system("TASKKILL /f /im chrome.exe")
        
        elif "maps" in query:
            os.system("TASKKILL /f /im chrome.exe")    

        elif "chrome" in query:
            os.system("TASKKILL /f /im chrome.exe")  

        elif "code" in query:
            os.system("TASKKILL /f /im code.exe")

    def Dict():
        Speak("Dictionary Activated")
        Speak("Tell me the problem")
        prob = takecommand()

        if "meaning" in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("meaning of","")
            result = diction.meaning(prob)
            Speak(f"The meaning for {prob} is {result}")

        elif "synonym" in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("synonym of","")
            result = diction.synonym(prob)
            Speak(f"The synonym for {prob} is {result}")

        elif "antonym" in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("antonym of","")
            result = diction.antonym(prob)
            Speak(f"The antonym for {prob} is {result}")

        Speak("Exited dictionary")    

    def Youtubeauto():
        Speak("What is you command?")
        come = takecommand()

        if "pause" in come:
            keyboard.press("space bar")
        elif "play" in come:
            keyboard.press("space bar")
        elif "mini screen" in come:
            keyboard.press("esc")
        elif "restart" in come:
            keyboard.press("0")   
        elif "mute" in come:
            keyboard.press(" m")   
        elif "skip" in come:
            keyboard.press("l")
        elif "increase volume" in come:
            keyboard.press("Up arrow")   
        elif "volume down" in come:
            keyboard.press("down arrow")       
        elif "back" in come:
            keyboard.press("j")   
        elif "full screen" in come:
            keyboard.press("f")
        elif "file mode" in come:
            keyboard.press("t")       

        Speak("Done Sir!")

    def Chrome_automation():
        Speak("What is your command sir")
        chrome_auto = takecommand()

        if "New browser window" in chrome_auto:
            keyboard.press_and_release("ctrl + n")
            Speak("your new browser is ready sir")

        elif "new tab" in chrome_auto:
            keyboard.press_and_release("ctrl + t")
            Speak("your new tab is ready sir")
        
        elif "close tab" in chrome_auto:
            keyboard.press_and_release("ctrl + w")
            Speak("done closing tab")
        
        elif "Back page" in chrome_auto:
            keyboard.press_and_release("Alt+Left Arrow")
            Speak("back page done sir")
        
        elif "Forward page" in chrome_auto:
            keyboard.press_and_release("Alt+Right Arrow")
            Speak(" page forwarded sir")    
        elif "minimise window" in chrome_auto:
            keyboard.press_and_release("Alt + Space + n")
            Speak("window minimized")                 

    def screenshot():
        Speak("ok boss, what should i name that file")
        path = takecommand()
        pathname = path + ".png"
        path1 = "C:\\Users\\Hunani Trading Co\\Pictures\\screenshots" + pathname
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\Hunani Trading Co\\Pictures\\screenshots")
        Speak("Here is your screenshot boss")

    def takehindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language="ur-PK")
                print(f"You said: {query}")

            except:
                return "none"

            return query.lower()        
    
    def Trans():
        Speak("Tell me the line: ")
        line = takehindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak("The translation for this line is: " + Text)

    def Temp():
        search = "temperature in Karachi"
        url = f"https://www.google.com/search?q={search}"
        f = requests.get(url)
        data = BeautifulSoup(f.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        Speak(f"The temperature outside is {temperature} celcius")

    while True:
        query = takecommand()
        if "hello" in query:
            Speak("Hello Sir , Jarvis here")
            Speak("Your perosnal Artificial intelligence assistant.")
            Speak("How may I help you?")

        elif "how are you" in query:
            Speak("I am fine Sir.")
            Speak("What about you?")   

        elif "bye" in query:
            Speak("Ok sir! Bye. You can call me anytime")
            Speak("Just say wake up jarvis")
            break

        elif "Youtube Search" in query:
            Speak("Ok sir! This is what I found for your search")
            query.replace("jarvis","")    
            query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            Speak("Done Sir! ")

        elif "Google search" in query:
            Speak("Ok sir! This is what I found for your search")
            query = query.replace("jarvis","")    
            query = query.replace("Google search","")
            pywhatkit.search(query)
            Speak("Done Sir! ")

        elif "website" in query:
            Speak("Ok sir! Launching....")
            query = query.replace("jarvis","")    
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = "https://wwww." + web1 + ".com"
            webbrowser.open(web2)
            Speak("Launched! ")

        elif "launch" in query:
            Speak("Tell me the name of the website")
            name = takecommand()
            web3 = "https://wwww." + name + ".com"
            webbrowser.open(web3)
            Speak("Done sir! ")

        # to open any website 
        elif "reddit" in query:
            Speak("Ok sir...")
            webbrowser.open("https://www.reddit.com/")
            Speak("Done sir! ")

        elif "music" in query:
            Music()      

        elif "wikipedia" in query:
            Speak("Searching wikipedia....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki}")

        elif "whatsapp message" in query:

            Whatsapp()    

        elif "screenshot" in query:
           screenshot()

        # open 
        elif "open facebook" in query:
            OpenApp()

        elif "open instagram" in query:
            OpenApp()
        elif "open file manager" in query:
            OpenApp()
        elif "open maps" in query:
            OpenApp()
        elif "open chrome" in query:
            OpenApp()
        elif "open code" in query:
            OpenApp() 
        elif "open youtube" in query:
            OpenApp()                       

        #close
        elif "close facebook" in query:
            CloseApp()
        elif "close instagram" in query:
            CloseApp()
        elif "close file manager" in query:
            CloseApp()
        elif "close maps" in query:
            CloseApp()
        elif "close chrome" in query:
            CloseApp()
        elif "close code" in query:
            CloseApp() 
        elif "close youtube" in query:
            CloseApp()                       
        # Youtube Automation
        elif "pause" in query:
           keyboard.press("k")
        elif "play" in query:
            keyboard.press("space bar")    
        elif "restart" in query:
            keyboard.press("0")   
        elif "mute" in query:
            keyboard.press("m")   
        elif "skip" in query:
            keyboard.press("l")   
        elif "back" in query:
            keyboard.press("j")   
        elif "full screen" in query:
            keyboard.press("f")
        elif "mini screen" in query:
            keyboard.press("esc")    
        elif "file mode" in query:
            keyboard.press("t") 
        elif "increase volume" in query:
            keyboard.press("Up arrow")   
        elif "volume down" in query:
            keyboard.press("down arrow")          
        elif "Youtube Tools" in query: 
            Youtubeauto()
            Speak("done sir!")

        # Chrome automation
        elif "New browser window" in query:
            keyboard.press_and_release("ctrl + n")

        elif "new tab" in query:
            keyboard.press_and_release("ctrl + t")
        
        elif "close tab" in query:
            keyboard.press_and_release("ctrl + w")
        
        elif "Back page" in query:
            keyboard.press_and_release("Alt+Left Arrow")
        
        elif "Forward page" in query:
            keyboard.press_and_release("Alt+Right Arrow") 
        elif "handle chrome" in query:
            Chrome_automation()  

        elif "tell me a joke" in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif "repeat my words" in query:
            Speak("Speak sir!")
            jj = takecommand()
            Speak(f"You said: {jj}")

        elif "my location" in query:
            Speak("ok sir! wait a second")
            webbrowser.open("https://www.google.com/maps/@24.9331712,67.0793728,11z")   

        #Dictionary
        elif "dictionary" in query:
            Dict()

        #Hindi Translation
        elif "translator" in query:
            Trans()

        #Remainder
        elif "remember that " in query:
            remeberMsg = query.replace("remember that","")
            rememberMsg = query.replace("jarvis","")
            Speak("You tell me to remind you that:" + remeberMsg)
            remember = open("D:/Jarvis1/data.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            remember = open("data.txt","r")
            Speak(f"You tell me to remember that: {remember.read()}")

        elif "google search" in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This is what i found on the web")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No speakable data available")    

        #Temperature
        elif "temperature" in query:
            Temp()

        #how to 
        elif "how to" in query:
            Speak("Getting data from the internet")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

TaskExecution()            