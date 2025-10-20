import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you!"
    elif "your name" in user_input:
        return "I'm your offline AI assistant."
    elif "bye" in user_input or "quit" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Offline AI Voice Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            farewell = "Goodbye! Have a nice day."
            print("Bot:", farewell)
            speak(farewell)
            break

        response = chatbot_response(user_input)
        print("Bot:", response)
        speak(response)

if __name__ == "__main__":
    main()
