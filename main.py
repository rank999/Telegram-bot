from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 13476379
api_hash = "43e2c95f17d4d4dcc21c547b4f018fe5"
session_string = "1BJWap1sBu6gY3ou1RujJF7ljQCrLseb2FUylKobxskdWedeWVpPb6RVOFS_01GhUAZd4xsmX1S3IjCct3rzhW66YXZkFc4foyHXE-AC4G10p2cp7SUagGNRMZJXjBhYapIQap0etp8tggw6J3k7dpmHTfiuU76C6BDHtr1Z9A3DFBDo7aN4fe5KnZm9ztYrzXynDjcDUwxNzQUSw39D4lltYSwzeKFydogZ0uQ6qM3QuV9lViC-7ad6zlYI0JqeDfnsVRwUrS8k-_1hxm1d2h3emeF9Wwz4v6DqLNjPrdkTPY9pF1B3gR4V2ydB9A78XxR2MgjoOYvTT1bHlkMa1KH0ztH1xhKE="

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(pattern="(?i)hello"))
async def handler(event):
    if event.is_private:
        await event.reply("Hi! I'm online and working 24/7 😎")

print("Userbot is starting...")
client.start()
print("Userbot is running. Waiting for messages...")
client.run_until_disconnected()
