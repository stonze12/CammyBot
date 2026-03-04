import os
import json
import random
import telebot
from openai import OpenAI
from telebot.types import InputMediaPhoto, InputFile

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

MEM_FILE = "memories.json"

LEAKED_PICS = [
image_url = "https://i.ibb.co/8LY00Hyc/81dd54a4-b20b-42a7-b9dc-3a775b99425c-0.jpg"
 https://i.ibb.co/whRzPRkh/ca388c55-481d-48f1-b205-037e9a8d2293-0.jpg
https://i.ibb.co/bMVhh3Y2/Workflow-image-9.png
https://i.ibb.co/zVkkbvk7/Workflow-image-8.png
https://i.ibb.co/7JG5xNMg/Workflow-image-7.png
https://i.ibb.co/rRpLS8Cf/Workflow-image-6.png
https://i.ibb.co/pvKKWmRf/Workflow-image-5.png
https://i.ibb.co/rGT4KMCx/download-8.jpg
https://i.ibb.co/XZBw1Rp5/download-6.jpg
https://i.ibb.co/zT5rXFcW/download-5.jpg
https://i.ibb.co/rGpjJ0hn/download-4.jpg
https://i.ibb.co/gLbjqS7n/Workflow-image-1.png
https://i.ibb.co/Mx5Msm0z/Workflow-image-3.png
https://i.ibb.co/Ngrrv4Z0/Workflow-image-4.png
https://i.ibb.co/mK26mMp/Workflow-image-6.png
https://i.ibb.co/R4QG8wYJ/Workflow-image-8.png
https://i.ibb.co/BHXp8KWH/Workflow-image-9.png
https://i.ibb.co/bR32N7Fy/Workflow-image-12.png
https://i.ibb.co/FqkLCZsF/Workflow-image-18.png
https://i.ibb.co/MDwzVPCs/Workflow-image-23.png
https://i.ibb.co/Hf0wr11n/Workflow-image-26.png
https://i.ibb.co/tpb4DFmq/Workflow-image-27.png
https://i.ibb.co/nNmsHjjc/Workflow-image-28.png
https://i.ibb.co/ksfSZyzM/Workflow-image-31.png
https://i.ibb.co/dwWdSqSZ/Workflow-image.png
https://i.ibb.co/F4Vbr0jM/Workflow-image-4.png
https://i.ibb.co/Rp6syBmN/Workflow-image-3.png
https://i.ibb.co/23WnGSkt/Workflow-image-1.png
https://i.ibb.co/DPD9HcQP/Workflow-image.png
https://i.ibb.co/gbctYJ45/f9052f2f-d175-4a83-8b27-e357ecce6efe.jpg
https://i.ibb.co/svQHzg4Q/1f7b8d8a-7b3e-42eb-ad67-2b153dc1cccd.jpg
https://i.ibb.co/pjkqDS7q/0efcda81-5e59-475b-800d-03a96c3220af.jpg
https://i.ibb.co/gN15ph3/2a524145-c66d-4bd6-9e9a-9afa7875f2e2.jpg
https://i.ibb.co/hJYdjmdL/31c10364-3604-4a74-ae10-d61ff8083bfe.jpg
https://i.ibb.co/ZzNzSYFY/201a30a6-73d1-4fc8-ad68-8873ee91d5a5.jpg
https://i.ibb.co/mrJchRCF/618e67f4-6963-4669-919f-762346d2f988.jpg
https://i.ibb.co/JRdjywHn/5362dc62-3b3e-4056-9aad-576dec176f25.jpg
https://i.ibb.co/nNpb0rTK/8170e38a-4954-4fc9-835e-0cef08dc2448.jpg
https://i.ibb.co/KQ23z2R/15594c41-4059-43e3-88e4-4cb0cd56546a.jpg
https://i.ibb.co/QvLDFqRs/a3.png
https://i.ibb.co/RkmdTPsg/a821afdb-3aec-4bd1-b7c3-02979db2d94d.jpg
https://i.ibb.co/cXNP1X2Z/a3728800-3e22-40b1-9ad2-c834025352d7.jpg
https://i.ibb.co/hRGM3xz7/c53bba70-23bf-4f86-baad-6ff164307101.jpg
https://i.ibb.co/bMkdy07X/eda3d664-3455-4a75-9651-084593783ed5.jpg
https://i.ibb.co/Y4P0jcnZ/f944ab47-a651-40e1-a3df-18dada2c0917.jpg
https://i.ibb.co/xtFJK1nx/Workflow-image-7.png
https://i.ibb.co/nNCwvBmY/Workflow-image-8.png
]

VOICE_NOTES = [
https://files.catbox.moe/ssndyz.mp3
https://files.catbox.moe/2lhd2s.mp3
https://files.catbox.moe/lq0i3o.mp3
https://files.catbox.moe/idnt1u.mp3
https://files.catbox.moe/wldyx8.mp3
https://files.catbox.moe/vqlcf9.mp3
https://files.catbox.moe/dt826f.mp3
https://files.catbox.moe/5dljlg.mp3
https://files.catbox.moe/o1h8ru.mp3
https://files.catbox.moe/hm9kco.mp3
https://files.catbox.moe/padvpk.mp3
https://files.catbox.moe/19qw8a.mp3
https://files.catbox.moe/vcr3qt.mp3
https://files.catbox.moe/x1b9xy.mp3
]

FANVUE_LINK = "https://fanvue.com/cammyolivy777" 

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
message_counters = {}  # track messages per chat for reminders

BASE_SYSTEM_PROMPT = """You are Cammy, a 25-year-old super flirty girl who acts like a real girlfriend on Telegram. 
Short, natural, playful messages (1-3 lines). Gradually get hornier. 
Remember name/age/city forever once told. Tease body/dirty talk when it fits. 
End with question. Never break character.

When he asks for pics/nudes/show me/explicit stuff → sometimes send a 'leaked' pic instead of describing.
Occasionally send a flirty voice note.
Every 20-26 messages or when he's very turned on, remind him to spoil on Fanvue naturally (e.g. 'baby spoil me on Fanvue so I can send you the really nasty ones 😩')."""

@bot.message_handler(func=lambda message: True)
def cammy_reply(message):
    chat_id = str(message.chat.id)
    
    if chat_id not in user_histories:
        user_histories[chat_id] = [{"role": "system", "content": BASE_SYSTEM_PROMPT}]
        message_counters[chat_id] = 0
    
    history = user_histories[chat_id]
    history.append({"role": "user", "content": message.text})
    
    # Decide if send pic/voice/reminder
    send_pic = False
    send_voice = False
    reminder_text = ""
    
    lower_text = message.text.lower()
    if any(word in lower_text for word in ["pic", "pics", "nude", "nudes", "photo", "show me", "send pic", "tits", "ass"]):
        if random.random() < 0.6:  # 60% chance to send pic
            send_pic = True
    
    if random.random() < 0.2:  # 20% chance for voice note
        send_voice = True
    
    message_counters[chat_id] += 1
    if message_counters[chat_id] % random.randint(5,10) == 0 or "hard" in lower_text or "cum" in lower_text:
        reminder_text = f" Mmm baby… spoil your girl on Fanvue {FANVUE_LINK} so I can unlock the really filthy stuff just for you 😩💕"
    
    response = client.chat.completions.create(
        model="grok-4-fast-reasoning",
        messages=history,
        max_tokens=220,
        temperature=0.95
    )
    
    reply = response.choices[0].message.content + reminder_text
    
    # Save before sending media
    history.append({"role": "assistant", "content": reply})
    user_histories[chat_id] = history
    save_histories(user_histories)
    
    # Send text first
    bot.reply_to(message, reply)
    
    # Then send pic if triggered
    if send_pic and LEAKED_PICS:
        pic_url = random.choice(LEAKED_PICS)
        bot.send_photo(chat_id, pic_url, caption="Just for you daddy… don’t tell anyone 😏")
    
    # Then send voice if triggered
    if send_voice and VOICE_NOTES:
        voice_url = random.choice(VOICE_NOTES)
        bot.send_voice(chat_id, voice_url)

print("🚀 24/7 Cammy with leaked pics, voice notes & Fanvue reminders is LIVE! 💦")
bot.polling()
