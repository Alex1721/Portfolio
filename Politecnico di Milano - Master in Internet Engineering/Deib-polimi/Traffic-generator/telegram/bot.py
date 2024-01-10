from pyrogram import Client, filters
import time
import random

api_id = 21452602
api_hash = '6f4666c4098cc9c49fefe5279c7cbc5e'
bot_token = '6906320273:AAE5XddM8IRPLmxjEUxZR82zifJAEqT1Adg'

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.private)
async def hello(client, message):
    while True:
        await message.reply("Hello from the telegram bot!")
        time.sleep(random.randint(1, 10))


app.run()