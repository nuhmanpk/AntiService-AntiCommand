import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message   
bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
 await message.reply_text("Ready to Work")

@bughunter0.on_message(filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()  

bughunter0.run()                              
