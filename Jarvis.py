import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import openai
import speech_recognition as sr
from googletrans import Translator

speaker=win32com.client.Dispatch("SAPI.Spvoice")

def ai(promt):
    import os
    import openai

    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{''.join(promt.split('open ai') [1:] ) }\n"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    """"{
         "id": "chatcmpl-7tFqfWry6Q3kfTom8dmegpk2wFM1Q",
         "object": "chat.completion",
         "created": 1693403317,
         "model": "gpt-3.5-turbo-0613",
         "choices": [
             {
                 "index": 0,
                 "message": {
                     "role": "assistant",
                     "content": "I am an AI language model developed by OpenAI called GPT-3. I am here to assist with any questions or tasks you might have. How can I help you today?"
                 },
                 "finish_reason": "stop"
             }
         ],
         "usage": {
             "prompt_tokens": 11,
             "completion_tokens": 37,
             "total_tokens": 48
         }
     }"""
    text=response["choices"][0]["message"]["content"]
    say(response["choices"][0]["message"]["content"])
    print(text)
    if not os.path.exists("openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(promt.split('open ai') [1:] ) }.txt","w") as f:
        f.write(text)

chatStr=""

def chat(promt):
    global chatStr
    openai.api_key = "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"
    chatStr+= f"Aman:{promt}\nJarvis:"
    print(chatStr)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{chatStr}"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["message"]["content"])
    chatStr+=response["choices"][0]["message"]["content"]

def say(txt):
    speaker.Speak(txt)
# def takeCommand():
#     # r=sr.Recognizer()
#     # with sr.Microphone(device_index=0) as source:
#     #     r.pause_threshold=2
#     #     r.non_speaking_duration=.5
#     #     audio=r.listen(source)
#     #     try:
#     #         print("Recognize")
#     #         query = r.recognize_google(audio, language="en-in")
#     #         print(f"User Said {query}")
#     #         return query
#     #     except Exception as e:
#     #         return "Some error occurred , Sorry From Jarvis "
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="en-in")
#     except:
#         return ""
#
#     query = str(query).lower()
#     return query
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi-IN")
    except:
        return ""

    query = str(query).lower()
    return query


# print(Listen())
# 2- Translator

def TransLationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}")
    return data


# 3 - connect

def MicExecution():
    query = Listen()
    data = TransLationHinToEng(query)
    return data

if __name__=="__main__":
    s = "Hello ,I am Jarvis,How can I help You Aman Sir"
    say(s)
    while True:
        print("Listening...")
        query = MicExecution()         #take Command
        # say(text)
        sites=[["youtube","https://youtube.com"],["google","https://google.com"],["Chat GPT","https://chat.openai.com/"]]
        if "open site" in query.lower():
            for site in sites:
                if f"open site {site[0]}".lower() in query.lower():
                    say(f"{site[0]} opening Aman ..")
                    webbrowser.open(f"{site[1]}")

        music = [['Dil Awara', 'C:\\Users\\Aman\\Downloads\\Dilawara.mp3'], ["maan meri jaan", 'C:\\Users\\Aman\\Downloads\\Maan.mp3']]
        if "open music" in query.lower():
            for mus in music:
                if f"open music {mus[0]}".lower() in query.lower():
                    say(f"{mus[0]} opening Aman ..")
                    musicpath = f"{mus[1]}"
                    os.system(f"start {musicpath}")



        if "the time" in query.lower():
            hr=datetime.datetime.now().strftime("%H")
            min=datetime.datetime.now().strftime("%M")
            say(f"Sir The Time is {hr}  and {min} minutes Aman")

        elif "open ai" in query.lower():
            say("Ok Aman")
            ai(query)

        elif "quit" in query.lower():
            say("bye Aman")
            quit()

        elif "chat reset" in query.lower():
            say("chat reseted")
            chatStr=""


        else:
            chat(query)


























