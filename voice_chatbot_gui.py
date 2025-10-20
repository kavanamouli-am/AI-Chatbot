import tkinter as tk
from tkinter import scrolledtext
import threading
import os
from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS
from playsound import playsound
import uuid

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speak(text):
    def run():
        temp_dir = os.path.join(os.getcwd(), "temp_audio")
        os.makedirs(temp_dir, exist_ok=True)
        
        filename = f"{uuid.uuid4()}.mp3"  # create unique filename
        filepath = os.path.join(temp_dir, filename)
        
        tts = gTTS(text=text, lang='en')
        tts.save(filepath)
        
        playsound(filepath)
        
        try:
            os.remove(filepath)  # delete after playing
        except Exception as e:
            print(f"Could not delete temp file: {e}")
        
    threading.Thread(target=run, daemon=True).start()

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def send_message():
    user_input = user_entry.get()
    if user_input.lower() == 'quit':
        root.destroy()
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    chat_window.config(state='disabled')
    user_entry.delete(0, tk.END)

    def handle_response():
        response = get_response(user_input)
        chat_window.config(state='normal')
        chat_window.insert(tk.END, "Bot: " + response + "\n")
        chat_window.config(state='disabled')
        chat_window.see(tk.END)
        speak(response)

    threading.Thread(target=handle_response).start()

root = tk.Tk()
root.title("AI Voice Chatbot")

chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, width=80, height=25, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=70, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10), expand=True, fill=tk.X)
user_entry.focus()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=(0,10), pady=(0,10))

root.mainloop()



