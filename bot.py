from pyrogram import Client, filters

# بياناتك الجديدة من موقع تيليجرام
api_id = 37707656
api_hash = "283a8c72f4c112f59ce14e5717605c9b"
bot_token = "8914465158:AAEoy6cxuvmsxne2aqATdPf_npZuZCDPEyQ" 

# إعداد البوت
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# معرفات القنوات
source_channel = -1002496748420
target_channel = -1003769157498

@app.on_message(filters.chat(source_channel))
def copy_message(client, message):
    message.copy(chat_id=target_channel)
    print("تم نسخ المنشور بنجاح!")

print("البوت يعمل الآن... أرسل شيئاً في القناة الأساسية!")
app.run()
