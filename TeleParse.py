from re import search
from telethon import TelegramClient
import asyncio

api_id = 10649685
api_hash = 'e4af0988d890d1f116c948c56626393c'
client = TelegramClient('anon', api_id, api_hash)

async def main():
  # Get all chats/users you are talking with
  dialogs = await client.get_dialogs()
  value = input("Please type in the keyword to search for: ")
  # for each of the chats, grab the messages
  # alternatively we could just do a global search
  for dialog in dialogs:
    messages = await client.get_messages(dialog.id, search=value)
    for message in messages:
      print(message)
with client:
  client.loop.run_until_complete(main())