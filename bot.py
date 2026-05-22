from pyrogram import Client, filters

# بياناتك الخاصة
api_id = 3479415
api_hash = "8a37c4085db8f17687c1d9dede24068"
bot_token = "8914465158:AAH9uuW7VKIywlAH0aJZXU-R6fygul8RtJ4"

# إنشاء البوت
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# معرفات القنوات
SOURCE_CHANNEL = -1002496748420
TARGET_CHANNEL = -1003769157498

@app.on_message(filters.chat(SOURCE_CHANNEL))
def forward_message(client, message):
    # يقوم البوت بنسخ الرسالة (Copy) للقناة الوجهة
    message.copy(chat_id=TARGET_CHANNEL)

print("البوت يعمل الآن، قم بنشر شيء في القناة الأساسية للتجربة...")
app.run()
