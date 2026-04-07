import asyncio
import os
from telethon import TelegramClient

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
GROUP_ID = int(os.environ["GROUP_ID"])
PHONE = os.environ["PHONE"]
SESSION = os.environ.get("SESSION", "")
MESAJ = "Merhaba, tanışmak isteyen😊"

client = TelegramClient("session", API_ID, API_HASH)

async def main():
    await client.start(phone=PHONE)
    while True:
        await client.send_message(GROUP_ID, MESAJ)
        await asyncio.sleep(5 * 60)

asyncio.run(main())
