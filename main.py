import openai
import speech_recognition as sr
import win32com.client as wincom
import webbrowser
import re,os
from config import apikey


openai.api_key = apikey

def ask_chatbot(prompt):#this fuction will pass the input to chat gpt and will return the response of chat gpt
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    if response and 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    
    return "I'm sorry, but I don't have a response for that."

def chatbot(chatbot_response):
    chatbot_response = ask_chatbot(user_input)
    print("Chatbot:", chatbot_response)
    speak.Speak(chatbot_response)


def website():
    try:
        comm=rec.recognize_google(audio) #here we decode the audio
        pattern = r'\bopen\s+(\w+)\b'
        match = re.search(pattern, comm)
        if match:
            web_site= match.group(1)
        url = "https://www." + web_site + ".com"  #here we load the website
        webbrowser.open(url)
        
        print("Website loaded sir")
        speak.Speak("website loaded sir")

    except:
        print("sorry I could not understand ")


def write(task):
    response=ask_chatbot(task)
    text=f"The task was - {task} \nOpen ai response is: \n {response}"
    
    if not os.path.exists("responses"):
        os.mkdir("responses")

    with open(f"responses/{task}.txt","w") as f:
        f.write(text)



rec = sr.Recognizer()
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak("Hi,I am JARVIS, how may I help you ")
print("Hi,I am JARVIS how may I help you ")

# Chat loop

while True:
    with sr.Microphone() as source:
        print("listening...")
        audio=rec.listen(source)

    try:
        user_input=rec.recognize_google(audio)
        print(user_input)

        if "close".lower() in user_input.lower():
            print("Goodbye sir")
            speak.Speak("goodbye sir")
            break

        elif "open".lower() in user_input.lower():
            website()
            print("Task completed sir")
            speak.Speak("Task completed sir ")

        elif"write".lower() in user_input.lower():
            write(user_input)
            print("Task completed sir")
            speak.Speak("Task completed sir")
            print("Please check your 'responses' folder")
            speak.Speak("please check your responses folder")
            
        else:
            chatbot(user_input)
        
        

    except:
        print("sorry I could not understand ")
        speak.Speak("sorry I could not understand")
