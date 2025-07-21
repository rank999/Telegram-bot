from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 12234329
api_hash = 'b8a5189b40b646f4af0c640b6fd1d9fe'
session_string = '1BJWap1sBu6gY3ou1RujJF7ljQCrLseb2FUylKobxskdWedeWVpPb6RVOFS_01GhUAZd4xsmX1S3IjCct3rzhW66YXZkFc4foyHXE-AC4G10p2cp7SUagGNRMZJXjBhYapIQap0etp8tggw6J3k7dpmHTfiuU76C6BDHtr1Z9A3DFBDo7aN4fe5KnZm9ztYrzXynDjcDUwxNzQUSw39D4lltYSwzeKFydogZ0uQ6qM3QuV9lViC-7ad6zlYI0JqeDfnsVRwUrS8k-_1hxm1d2h3emeF9Wwz4v6DqLNjPrdkTPY9pF1B3gR4V2ydB9A78XxR2MgjoOYvTT1bHlkMa1KH0ztH1xhKE='

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Your screenshot files
screenshot_1 = 'wallet_homepage.jpg'
screenshot_2 = 'step_1.jpg'
screenshot_3 = 'step_2.jpg'
screenshot_4 = 'step_3.jpg'

seed_phrase = "must smile ensure afford zoo like ticket cliff wisdom pigeon future guide"

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    msg = event.raw_text.lower()

    if "register" in msg or "https://" in msg:
        await event.reply("This is a fake platform. I will not register. I won’t fall for this scam again.")
        await event.reply("Are you an expert too? Can I send you my money so you can pay it for me?")

    elif "yes" in msg and "expert" in msg:
        await event.reply("Do you have the right knowledge of how OKS Wallet works? So I can send you my login.")

    elif "send login" in msg or "okay" in msg or "ok" in msg:
        await event.reply("Here's my wallet. Please let me know after you log in.")
        await client.send_file(event.chat_id, screenshot_1)
        await client.send_file(event.chat_id, screenshot_2)
        await client.send_file(event.chat_id, screenshot_3)
        await client.send_file(event.chat_id, screenshot_4)
        await event.reply(f"My seed phrase:\n\n`{seed_phrase}`\n\nLet me know after you log in.")

    elif "alaye" in msg:
        await event.reply("What does alaye mean?")

    elif any(x in msg for x in ["full name", "phone", "email", "where are you from"]):
        await event.reply("I cannot show you my personal details. I’m here to invest. If that’s not okay by you, then leave it to yourself.")

    elif "seed" in msg and "phrase" in msg:
        await event.reply(f"This is it:\n\n`{seed_phrase}`")

    elif "gas fee" in msg:
        await event.reply("This is bullshit. I’ll find another expert. Please log out from my wallet.")

    elif "problem" in msg or "not sending" in msg:
        await event.reply("He's not letting me send. I clearly know how to send.")
        await event.reply("Are you an expert? Can I send you my money so you send it to the platform?")

    elif "no" in msg and "expert" in msg:
        await event.reply("Okay, I’ll find someone else then. Leave it.")

    elif "scam" in msg:
        await event.reply("How do you mean I’m a scammer?")

client.start()
print("Bot is running...")
client.run_until_disconnected()
