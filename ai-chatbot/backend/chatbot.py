import datetime
import random

def get_response(text):
    text = text.lower()

    # greetings
    if "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help you?"

    elif "how are you" in text:
        return "I am fine, thank you! 😊"

    elif "what is your name" in text:
        return "I am an AI Chatbot 🤖"

    elif "who made you" in text:
        return "I was created by a developer using Python 😄"

    # AI related
    elif "what is ai" in text:
        return "AI means Artificial Intelligence 🤖"

    elif "what is machine learning" in text:
        return "Machine Learning is a part of AI that learns from data 📊"

    elif "what is python" in text:
        return "Python is a powerful programming language 🐍"

    # personal questions
    elif "what can you do" in text:
        return "I can answer your questions, tell jokes, and help you 😊"

    elif "are you real" in text:
        return "No, I am a virtual AI chatbot 🤖"

    # time & date
    elif "time" in text:
        now = datetime.datetime.now()
        return "Current time is " + now.strftime("%H:%M:%S")

    elif "date" in text:
        today = datetime.date.today()
        return "Today's date is " + str(today)

    # calculator
    elif "+" in text or "-" in text or "*" in text or "/" in text:
        try:
            result = eval(text)
            return "Result is: " + str(result)
        except:
            return "Invalid calculation 😅"

    # fun
    elif "joke" in text:
        return "Why did the computer go to school? To improve its memory 😂"

    elif "motivation" in text:
        return "Believe in yourself! You can do anything 💪🔥"

    elif "good morning" in text:
        return "Good morning! ☀️ Have a great day!"

    elif "good night" in text:
        return "Good night! 🌙 Sweet dreams!"

    # goodbye
    elif "bye" in text:
        return "Goodbye! 👋 Have a nice day!"

    # 🔥 SMART DEFAULT (unknown questions)
    else:
        replies = [
            "Hmm 🤔 I'm not sure about that.",
            "I'm still learning, can you ask something else? 😊",
            "Interesting question! I don't have an answer yet 😅",
            "Sorry, I didn't understand that. Try asking differently 👍"
        ]
        return random.choice(replies)