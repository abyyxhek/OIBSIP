import tkinter as tk
from datetime import datetime
import re

def get_response(msg):
    msg = msg.lower()

    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", msg):
        return "Hey there! How can I assist you today?"
    elif re.search(r"\b(your name|who are you)\b", msg):
        return "I'm Jarvis , your virtual assistant 🤖"
    elif re.search(r"\b(who created you|your creator|developer)\b", msg):
        return "I was created by Abishek as part of a project!"
    elif re.search(r"\b(time)\b", msg):
        return "The current time is: " + datetime.now().strftime("%H:%M:%S")
    elif re.search(r"\b(date)\b", msg):
        return "Today's date is: " + datetime.now().strftime("%Y-%m-%d")
    elif re.search(r"\b(day)\b", msg):
        return "It's " + datetime.now().strftime("%A")
    elif re.search(r"\b(joke|funny)\b", msg):
        return "Why don't scientists trust atoms? Because they make up everything! 😂"
    elif re.search(r"\b(weather)\b", msg):
        return "I'm not connected to the internet, but it's always a good day to code! ☀️"
    elif re.search(r"\b(motivate|motivation)\b", msg):
        return "Believe in yourself! Every expert was once a beginner. 💪"
    elif re.search(r"\b(bye|exit|quit)\b", msg):
        return "Goodbye! Have a productive day. 👋"
    else:
        return "Hmm... I didn’t understand that. Try asking something else."

def send_message():
    user_msg = entry.get()
    chat_log.insert(tk.END, "You: " + user_msg + "\n")
    response = get_response(user_msg)
    chat_log.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Rule-Based ChatBot")

chat_log = tk.Text(window, height=20, width=50, bg="black", fg="white", font=("Arial", 12))
chat_log.pack()

entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(pady=5)

send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack()

window.mainloop()
