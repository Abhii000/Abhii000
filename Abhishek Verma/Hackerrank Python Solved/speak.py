#make a program that convert inout text to speech using pyttsx3 speed of person is 190
import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello. welcome to the program")
engine.runAndWait()
engine.stop()
print("Done")
#engine.save_to_file("Hello World", "hello.mp3")
