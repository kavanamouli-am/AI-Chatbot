import pyttsx3
import time

engine = pyttsx3.init()

texts = ["Hello!", "How can I help you?", "This is a test for multiple speeches"]

for t in texts:
    print(f"Speaking: {t}")
    engine.say(t)
    engine.runAndWait()
    time.sleep(0.5)
