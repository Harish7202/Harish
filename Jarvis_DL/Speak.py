import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set voice (adjust as needed)
engine.setProperty('rate', 180)  # Adjust speech rate if needed

def speak(Text):
    print("     ")
    print(f"J.A.R.V.I.S: {Text}")
    engine.say(Text)
    engine.runAndWait()
    print("     ")
