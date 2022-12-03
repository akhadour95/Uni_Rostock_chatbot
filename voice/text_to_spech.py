import subprocess
from gtts import gTTS
from playsound import playsound
import os


# The text that you want to convert to audio
mytext = 'Welcome to Innovate Yourself!'
# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language)
# Saving the converted audio in a mp3 file named
# welcomes
myobj.save("C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3")
# Playing the converted file
#subprocess.call(['mpg321' ".C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3", '--play-and-exit'])
playsound('C:\\Users\\akhadour\\Desktop\\FAQ_Uni_rostock_chatbot\\records\\welcome.mp3')

