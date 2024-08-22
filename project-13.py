import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import openai
# from config import apikey


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

# chatStr=""
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key=apikey
#     chatStr=f"Me:{query}\n AI:"
#     response=openai.Completion.create(
#         model="text.davinci-003",
#         prompt=chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )   
#     speak(response["choices"][0]["text"]) 
#     chatStr+=f"{response["choices"][0]["text"]}\n"
#     return response["choices"][0]["text"]

#     with open(f"openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
#         f.write(text) 
    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak(" क्या कर रही हो")
    
def greet():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Goog morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
        
    speak("I am your A I assistant, How may i help you")
    
    
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.pause_threshold=1
        r.energy_threshold = 400 

        audio=r.listen(source)
    
    try:
        print("Recognising")
        query=r.recognize_google (audio,language='en-US')
        print(f"You said : {query}")
        
    except Exception as e:
        print("Could you repeat it again")
        return "None"
    return query 
    
    
    
if __name__=="__main__":
    greet()
    while True:
       query= take().lower()
    #    sites=[["youtube","youtube.com"],["google","google.com"],["wikipedia","wikipedia.com"],] 
    #    for site in sites:
    #        if site[0] in query:
    #            speak(f"opening {site[0]}")
    #            webbrowser.open(site[1])
       if 'wikipedia' in query:
           speak("Searching wikipedia")
           query=query.replace("wikipedia"," ")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
           
      
       elif 'open google' in query:
           speak("opening google")
           webbrowser.open('google.com')
           
       elif 'open youtube' in query:
           speak("opening youtube")
           webbrowser.open( 'https://www.youtube.com/')
        
           
       elif 'open code' in query:
           speak("opening cwh")
           webbrowser.open('https://www.youtube.com/codeWithHarry')
           
       elif 'open python folder' in query:
        #    speak("opening python")
           py_dir=r'F:\Python' 
           os.startfile(py_dir)
           speak("Opening Python folder")
           
       elif 'time' in query:
           strftime=datetime.datetime.now().strftime('%H:%M:%S')
           print(strftime)
           speak(strftime)
           
       elif 'vs code' in query:
           path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           speak("Opening Visual Code")
           os.startfile(path)
    
       elif 'chat gpt' in query:
           path='https://chatgpt.com/?sso=&oai-dm=1'
           speak("Opening chat gpt")
           os.startfile(path)
           
           
        #   can send mail also
       elif 'stop' in query:
           speak("Thank you have a nice day")
           exit()
    
       else:
           speak(f"You said {query}")
           
    #    else:
    #        chat(query)