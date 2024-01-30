import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

import openai



def AI(prompt):
    openai.api_key='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'
    text=f'Openai Responsde to the prompt:{prompt}\n****************\n\n'
    
    response = openai.completions.create(
    model="gpt-3.5-turbo-1106",
    prompt=prompt,
    temperature=1,
    max_tokens=4096,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    text+=response['choices'][0]['text']
    if not os.path.exists('Openai'):
        os.mkdir('Openai')
    with open(f'Openai/{"".join(prompt.split(openai)[1:])}','w') as f:
        f.write(text)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Veronica Sir... Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 300 
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":

    wishMe()
    while True:

        query = takeCommand().lower()


        defaultAppList=[['code',"C:\\Users\\abhay\\PycharmProjects\\Microsoft VS Code\\Microsoft VS Code\\Code.exe"],['VLC',"C:\\Program Files\\VideoLAN\\VLC\\Vlc.exe"],['chrome','C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe']]


        webSitesList=[["open wikipedia", 'wikipedia.com'],['open youtube','https://www.youtube.com'],['open google','google.com'],['open stack Overflow','stacoverflow.com'],["anime",'https://aniwatch.to/home'],['open whatsApp','https://web.whatsapp.com/'],['open spotify','https://open.spotify.com'],['download movie','https://moviesnation.dev'],['regex','https://regexr.com/']]



        for i in defaultAppList:
            if f'open {i[0]}'.lower() in query:
                codePath = i[1]
                os.startfile(codePath)


        for i in webSitesList:
            if i[0].lower() in query:
                webbrowser.open_new_tab(i[1])



        if 'on wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)    
            speak(f"Sir, the time is {strTime}")


        
        elif query in ["thankYou",'thanks','thank','thank u']:
            speak("welcome sir...")
            speak('Is there any thing else i can help you with?...')
            query=takeCommand().lower()
            if "no" in query:
                speak("have a good day sir...")
                exit()
        

        elif "Using AI".lower() in query:
            AI(prompt=query)



        


