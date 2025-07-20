from telethon import TelegramClient, events

api_id = 13476379
api_hash = '43e2c95f17d4d4dcc21c547b4f018fe5'

client = TelegramClient("userbot", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:
        await event.reply("Hello! I'm online 24/7 😎")

client.start()
client.run_until_disconnected()