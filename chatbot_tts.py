import os
from openai import OpenAI
import pyttsx3

# 1️⃣ Set your API key
# os.environ["OPENAI_API_KEY"] = # Replace with your API key
import os
api_key = os.getenv("OPENAI_API_KEY")

# 2️⃣ Initialize OpenAI Client
client = OpenAI()

# 3️⃣ Initialize text-to-speech engine
engine = pyttsx3.init()

print("AI Voice Chatbot (type 'quit' to exit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    try:
        # 4️⃣ Send user input to OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast + cheap
            messages=[
                {"role": "system", "content": "You are a friendly chatbot."},
                {"role": "user", "content": user_input}
            ]
        )

        bot_reply = response.choices[0].message.content
        print(f"Bot: {bot_reply}")

        # 5️⃣ Speak the reply
        engine.say(bot_reply)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")
