import requests
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import subprocess

from pydub import AudioSegment
from pydub.playback import play
import  os
import time

print("Printed immediately.")



language = 'en'
bot_message = ""
message = ""
while bot_message != "Bye":
    

   r = sr.Recognizer()                 
   with sr.Microphone() as source:     
     audio = r.listen(source)        
     try:
        message = r.recognize_google(audio)    
        print("You said : {}".format(message))
     except:
        print("Sorry could not recognize your voice")    
    
   if len(message)==0:
        continue
    
   print("sending message")
    
   r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    
   print("Bot says, ",end=' ')
   for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
   voice_message = gTTS(text=bot_message, lang=language)

   voice_message.save("C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3")
   playsound("C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3", True)
   os.remove("C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3")