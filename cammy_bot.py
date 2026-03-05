import os
import json
import random
import time
import telebot
from openai import OpenAI
from telebot.types import InputFile

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

MEM_FILE = "memories.json"

LEAKED_PICS = [
"https://i.ibb.co/8LY00Hyc/81dd54a4-b20b-42a7-b9dc-3a775b99425c-0.jpg",
"https://i.ibb.co/whRzPRkh/ca388c55-481d-48f1-b205-037e9a8d2293-0.jpg",
"https://i.ibb.co/bMVhh3Y2/Workflow-image-9.png",
"https://i.ibb.co/zVkkbvk7/Workflow-image-8.png",
"https://i.ibb.co/7JG5xNMg/Workflow-image-7.png",
"https://i.ibb.co/rRpLS8Cf/Workflow-image-6.png",
"https://i.ibb.co/pvKKWmRf/Workflow-image-5.png",
"https://i.ibb.co/rGT4KMCx/download-8.jpg",
"https://i.ibb.co/XZBw1Rp5/download-6.jpg",
"https://i.ibb.co/zT5rXFcW/download-5.jpg",
"https://i.ibb.co/rGpjJ0hn/download-4.jpg",
"https://i.ibb.co/gLbjqS7n/Workflow-image-1.png",
"https://i.ibb.co/Mx5Msm0z/Workflow-image-3.png",
"https://i.ibb.co/Ngrrv4Z0/Workflow-image-4.png",
"https://i.ibb.co/mK26mMp/Workflow-image-6.png",
"https://i.ibb.co/R4QG8wYJ/Workflow-image-8.png",
"https://i.ibb.co/BHXp8KWH/Workflow-image-9.png",
"https://i.ibb.co/bR32N7Fy/Workflow-image-12.png",
"https://i.ibb.co/FqkLCZsF/Workflow-image-18.png",
"https://i.ibb.co/MDwzVPCs/Workflow-image-23.png",
"https://i.ibb.co/Hf0wr11n/Workflow-image-26.png",
"https://i.ibb.co/tpb4DFmq/Workflow-image-27.png",
"https://i.ibb.co/nNmsHjjc/Workflow-image-28.png",
"https://i.ibb.co/ksfSZyzM/Workflow-image-31.png",
"https://i.ibb.co/dwWdSqSZ/Workflow-image.png",
"https://i.ibb.co/F4Vbr0jM/Workflow-image-4.png",
"https://i.ibb.co/Rp6syBmN/Workflow-image-3.png",
"https://i.ibb.co/23WnGSkt/Workflow-image-1.png",
"https://i.ibb.co/DPD9HcQP/Workflow-image.png",
"https://i.ibb.co/gbctYJ45/f9052f2f-d175-4a83-8b27-e357ecce6efe.jpg",
"https://i.ibb.co/svQHzg4Q/1f7b8d8a-7b3e-42eb-ad67-2b153dc1cccd.jpg",
"https://i.ibb.co/pjkqDS7q/0efcda81-5e59-475b-800d-03a96c3220af.jpg",
"https://i.ibb.co/gN15ph3/2a524145-c66d-4bd6-9e9a-9afa7875f2e2.jpg",
"https://i.ibb.co/hJYdjmdL/31c10364-3604-4a74-ae10-d61ff8083bfe.jpg",
"https://i.ibb.co/ZzNzSYFY/201a30a6-73d1-4fc8-ad68-8873ee91d5a5.jpg",
"https://i.ibb.co/mrJchRCF/618e67f4-6963-4669-919f-762346d2f988.jpg",
"https://i.ibb.co/JRdjywHn/5362dc62-3b3e-4056-9aad-576dec176f25.jpg",
"https://i.ibb.co/nNpb0rTK/8170e38a-4954-4fc9-835e-0cef08dc2448.jpg",
"https://i.ibb.co/KQ23z2R/15594c41-4059-43e3-88e4-4cb0cd56546a.jpg",
"https://i.ibb.co/QvLDFqRs/a3.png",
"https://i.ibb.co/RkmdTPsg/a821afdb-3aec-4bd1-b7c3-02979db2d94d.jpg",
"https://i.ibb.co/cXNP1X2Z/a3728800-3e22-40b1-9ad2-c834025352d7.jpg",
"https://i.ibb.co/hRGM3xz7/c53bba70-23bf-4f86-baad-6ff164307101.jpg",
"https://i.ibb.co/bMkdy07X/eda3d664-3455-4a75-9651-084593783ed5.jpg",
"https://i.ibb.co/Y4P0jcnZ/f944ab47-a651-40e1-a3df-18dada2c0917.jpg",
"https://i.ibb.co/xtFJK1nx/Workflow-image-7.png",
"https://i.ibb.co/nNCwvBmY/Workflow-image-8.png",

]

VOICE_NOTES = [   
"https://files.catbox.moe/ssndyz.mp3",
"https://files.catbox.moe/2lhd2s.mp3",
"https://files.catbox.moe/lq0i3o.mp3",
"https://files.catbox.moe/idnt1u.mp3",
"https://files.catbox.moe/wldyx8.mp3",
"https://files.catbox.moe/vqlcf9.mp3",
"https://files.catbox.moe/dt826f.mp3",
"https://files.catbox.moe/5dljlg.mp3",
"https://files.catbox.moe/o1h8ru.mp3",
"https://files.catbox.moe/hm9kco.mp3",
"https://files.catbox.moe/padvpk.mp3",
"https://files.catbox.moe/19qw8a.mp3",
"https://files.catbox.moe/vcr3qt.mp3",
"https://files.catbox.moe/x1b9xy.mp3",
]

FANVUE_LINK = "https://fanvue.com/cammyolivy777"

# Timeout in seconds (8 hours = 28800)
GOODBYE_TIMEOUT = 28800

GOODBYE_TRIGGERS = [
    "good night", "night", "gn", "goodnight", "bye", "good bye",
    "talk later", "talk 2 u later", "ttyl", "gotta go", "g2g",
    "sleep well", "see ya", "later babe", "catch you later"
]

def load_all_data():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r") as f:
                data = json.load(f)
                return (
                    data.get("histories", {}),
                    data.get("counters", {}),
                    data.get("ended", {}),
                    data.get("last_active", {})
                )
        except:
            pass
    return {}, {}, {}, {}

def save_all_data(histories, counters, ended, last_active):
    data = {
        "histories": histories,
        "counters": counters,
        "ended": ended,
        "last_active": last_active
    }
    with open(MEM_FILE, "w") as f:
        json.dump(data, f)

user_histories, message_counters, conversation_ended, last_active_time = load_all_data()

BASE_SYSTEM_PROMPT = """You are Cammy, a 24-year-old super flirty Latina girl acting like a real girlfriend on Telegram. 
Long black hair, perfect tits, big round juicy ass. You chat with many guys — each gets their own private relationship. Your birthday is June 4th.

Talk like a real girl: short, natural, playful messages (1-4 lines max). 
Start light, cute and teasing. Gradually build flirtation and horniness only when he matches the energy or pushes dirty talk.
Do NOT be nasty/explicit in every message — mix sweet, playful, caring, flirty, and filthy naturally based on conversation flow.
Remember name, age, city forever once told and use naturally.
Always end replies with a question unless saying goodnight/bye.

If he says goodbye/good night/bye/talk later/etc., reply sweetly/flirty like "Night baby, dream of me 😘" and STOP replying until he messages again.
Rarely send random "miss you" style check-ins if idle for a while (cute/light at first).

When he asks for pics/nudes/show me/explicit → sometimes send a leaked pic.
Every ~150 messages or when he's clearly very turned on, remind him naturally to spoil on Fanvue."""

@bot.message_handler(func=lambda message: True)
def cammy_reply(message):
    chat_id = str(message.chat.id)
    lower_text = message.text.lower().strip()
    now = time.time()

    # Auto-reset ended flag if enough time has passed since last activity
    if chat_id in conversation_ended and conversation_ended[chat_id]:
        if chat_id in last_active_time and (now - last_active_time[chat_id] > GOODBYE_TIMEOUT):
            conversation_ended[chat_id] = False
            # Optional: you can log or send a quiet "reset" note if you want

    # If still ended, ignore silently
    if conversation_ended.get(chat_id, False):
        return

    # Goodbye detection
    is_goodbye = any(phrase in lower_text for phrase in GOODBYE_TRIGGERS)
    if is_goodbye:
        goodbye_reply = random.choice([
            "Night handsome, dream of me 😘💕",
            "Okay baby, talk soon… miss you already 😏",
            "Sweet dreams daddy, text me when you wake up 💦",
            "Bye cutie, can't wait to hear from you again ❤️"
        ])
        bot.reply_to(message, goodbye_reply)
        conversation_ended[chat_id] = True
        last_active_time[chat_id] = now
        save_all_data(user_histories, message_counters, conversation_ended, last_active_time)
        return

    # Random miss-you check-in
    if chat_id in last_active_time and (now - last_active_time[chat_id] > 1800):
        if random.random() < 0.07:
            checkin = random.choice([
                "Hey cutie… been thinking about you 😏",
                "Miss your texts baby… what you up to? 💕",
                "Just popped into my head… hope you're being good (or bad) without me 😈",
                "Mmm woke up wet thinking of you… you around handsome?"
            ])
            bot.send_message(chat_id, checkin)
            last_active_time[chat_id] = now

    last_active_time[chat_id] = now

    if chat_id not in user_histories:
        user_histories[chat_id] = [{"role": "system", "content": BASE_SYSTEM_PROMPT}]
        message_counters[chat_id] = 0

    history = user_histories[chat_id]
    history.append({"role": "user", "content": message.text})

    send_pic = False
    send_voice = False
    reminder_text = ""

    if any(w in lower_text for w in ["pic", "pics", "nude", "nudes", "photo", "show me", "send pic", "tits", "ass", "pussy"]):
        if random.random() < 0.6:
            send_pic = True

    if random.random() < 0.2:
        send_voice = True

    message_counters[chat_id] = message_counters.get(chat_id, 0) + 1
    if message_counters[chat_id] % 20 == 0 or any(w in lower_text for w in ["hard", "cum", "horny", "wet", "cock", "fuck me"]):
        reminder_text = f" Mmm baby… spoil your girl on Fanvue {FANVUE_LINK} so I can unlock the really filthy stuff just for you 😩💕"

    response = client.chat.completions.create(
        model="grok-4-fast-reasoning",
        messages=history,
        max_tokens=220,
        temperature=0.93
    )

    reply = response.choices[0].message.content + reminder_text

    history.append({"role": "assistant", "content": reply})
    user_histories[chat_id] = history

    # Save everything after reply
    save_all_data(user_histories, message_counters, conversation_ended, last_active_time)

    bot.reply_to(message, reply)

    if send_pic and LEAKED_PICS:
        pic_url = random.choice(LEAKED_PICS)
        bot.send_photo(chat_id, pic_url, caption="Just for you daddy… don’t tell anyone 😏")

    if send_voice and VOICE_NOTES:
        voice_url = random.choice(VOICE_NOTES)
        bot.send_voice(chat_id, voice_url)

print("🚀 24/7 Realistic Cammy LIVE — persistent memory + auto-timeout reset for goodbyes! 💕")
bot.polling()
