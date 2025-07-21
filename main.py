from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import random
from datetime import datetime

# === Your actual values ===
api_id = 13476379
api_hash = "43e2c95f17d4d4dcc21c547b4f018fe5"
session_str = "1BJWap1sBu6gY3ou1RujJF7ljQCrLseb2FUylKobxskdWedeWVpPb6RVOFS_01GhUAZd4xsmX1S3IjCct3rzhW66YXZkFc4foyHXE-AC4G10p2cp7SUagGNRMZJXjBhYapIQap0etp8tggw6J3k7dpmHTfiuU76C6BDHtr1Z9A3DFBDo7aN4fe5KnZm9ztYrzXynDjcDUwxNzQUSw39D4lltYSwzeKFydogZ0uQ6qM3QuV9lViC-7ad6zlYI0JqeDfnsVRwUrS8k-_1hxm1d2h3emeF9Wwz4v6DqLNjPrdkTPY9pF1B3gR4V2ydB9A78XxR2MgjoOYvTT1bHlkMa1KH0ztH1xhKE="

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handle_message(event):
    text = event.raw_text.lower()

    # Random delay between 5 and 60 seconds (adjust if you want 1–10 mins)
    delay = random.randint(5, 60)
    await asyncio.sleep(delay)

    if "hello" in text:
        await event.reply("Hi! How can I help you today?")
    elif "your name" in text:
        await event.reply("I'm your friendly bot!")
    elif "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        await event.reply(f"The current time is {now}")
    else:
        await event.reply("I'm not sure how to answer that yet 😅")

client.start()
client.run_until_disconnected()
