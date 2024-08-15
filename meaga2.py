import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests




recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "130d1efcc2024a5e9b30d4cdb8f206d1"


def speak(text):
    engine.say(text)
    engine.runAndWait()





    
    

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        # Extract the song name after "play"
        song = " ".join(c.lower().split(" ")[1:])
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            print(f"Song '{song}' not found in the music library.")
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
         data = r.json()
         articles = data.get("articles", [])
         
         print("Headlines:")
         for article in articles:
          speak(article ['title'])
# ...


 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

