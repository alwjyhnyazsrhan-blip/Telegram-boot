from pyrogram import Client, filters

# بياناتك التي استخرجتها من my.telegram.org
api_id = 34979415
api_hash = "8a37c4085db8f17687c1d9dede24068"
bot_token = "8914465158:AAEoy6cxuvmsxne2aqATdPf_npZuZCDPEyQ"

# إعداد البوت
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# المعرفات التي زودتني بها (مع إضافة -100 للقنوات)
source_channel = -1002496748420
target_channel = -1003769157498

@app.on_message(filters.chat(source_channel))
def copy_message(client, message):
    # يقوم البوت بنسخ الرسالة للقناة الثانية
    message.copy(chat_id=target_channel)
    print("تم نسخ منشور جديد!")

print("البوت يعمل الآن، بانتظار المنشورات...")
app.run()
