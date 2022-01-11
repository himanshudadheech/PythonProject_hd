import pyttsx3 #pip install 
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui  /// screenshot
import psutil #pip install psutil  //cpu stats
import pyjokescli #pip install pyjokes
from wikipedia.wikipedia import search

engine = pyttsx3.init()

# engine.say("Today is friday")
# engine.runAndWait() #pauses the function util say function completes



voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("Hello for Function speak")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year =int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Current date Is : ")
    speak(year)
    speak(month)
    speak(day)

def wishme():
    speak("Welcome Back Sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak("Good Morning sir!!")
    elif hour > 12 and hour < 18:  
        speak("Good After Noon Sir!!")
    elif hour >=18 and hour <= 24:
        speak("Good Evening Sir!!")
    else:
        speak("Good Night Sir!!")    
    
    speak("HimBot at your service How Can i help You!")

#taking command from user voice

def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
    audio = r.listen(source)   
    print("Listening...")
    r.pause_threshold =1
    audio = r.listen(source)

    try:
        print("Recognizing...")
        r.adjust_for_ambient_noise(source)
        query = r.recognize(audio)
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        speak("Say That Again Please...!!")

        return "None"         
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login("sender@gmail.com","sender paasword")
    server.sendmail("sender@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\Python Project jarvis\ss.png")   

def cpu():
        usage = str(psutil.cpu_percent())
        speak("Cpu is at"+usage)
        battry = psutil.sensors_battery
        speak("battery is at")
        speak(battry.percent) 

def jokes():
 speak(pyjokescli.get_joke())    

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()       
        elif "date" in query:
            date()
        elif  "bye" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences =2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = "reciver@gmail.com"
                sendemail(to,content)
                speak("Mail Sent Successfully!!")
            except Exception as e:
                speak(e)
                speak("Unable to Send Email")    
        elif "search in chrome" in query:
              speak("What Should I Search For You?")     
             # chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s"
              searchh = takecommand().lower()
              wb.open("https://" + searchh + ".com")
              quit()
        elif "logout" in query:
            os.system("shutdown - 1")      
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")   
        elif "restart" in query:
            os.system("shutdown /r /t 1")   

        elif "Play songs" in query:
            song_dir = "E:\Himanshu dadheech\personal\audio\filmora ncs song"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0])) 

        elif "remember that" in query:
            speak("What Should I remember?") 
            data = takecommand()
            speak("You said me to remember" + data)
            remember = open("data.txt","w")
            remember.os.write(data)
            remember.close() 
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You Said me to remeber that"+ remember.read())             
        elif "screenshot" in query:
            screenshot()
            speak("done !!") 

        elif  "cpu" in query:
            cpu()  
        elif "joke" in query:
            jokes()        
       
    

