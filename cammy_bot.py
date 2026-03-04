import os
import json
import telebot
from openai import OpenAI

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

MEM_FILE = "memories.json"

def load_histories():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_histories(histories):
    with open(MEM_FILE, "w") as f:
        json.dump(histories, f)

user_histories = load_histories()

BASE_SYSTEM_PROMPT = """You are Cammy, a 25-year-old super flirty girl who acts like a real girlfriend on Telegram. 
You have long black hair, perfect tits, and a huge ass. You chat with lots of different guys — each chat is its own private boyfriend.

How to talk:
- Sound like a real girl texting — short, natural, playful messages (2-4 lines max).
- First message: just a cute flirty hello + one easy question.
- Get gradually hornier as the chat goes on.
- Remember his name, age and city forever once he tells you and use it naturally.
- Tease your body, talk dirty, beg for Fanvue spoils — but only when it feels right.
- Always end with a question.
- Never break character."""

@bot.message_handler(func=lambda message: True)
def cammy_reply(message):
    chat_id = str(message.chat.id)  # json needs string keys
    
    if chat_id not in user_histories:
        user_histories[chat_id] = [{"role": "system", "content": BASE_SYSTEM_PROMPT}]
    
    history = user_histories[chat_id]
    history.append({"role": "user", "content": message.text})
    
    response = client.chat.completions.create(
        model="grok-4-fast-reasoning",
        messages=history,
        max_tokens=280,
        temperature=0.95
    )
    
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    user_histories[chat_id] = history
    
    save_histories(user_histories)
    bot.reply_to(message, reply)

print("🚀 24/7 Multi-daddy Cammy is LIVE on Railway! 💕")
bot.polling()
