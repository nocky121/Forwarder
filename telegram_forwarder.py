import os
import re
import asyncio
from telethon import TelegramClient, events

# Load environment variables from Heroku Config Vars
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')
target_channel = os.environ.get('TARGET_CHANNEL')

# Define the source channel to monitor
source_channel = 'lottery_9_7'

# Unique session name for each environment
session_name = 'unique_session_name'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Function to handle incoming messages
@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message_text = event.message.message
    # Check if the message contains the numbers 8, 24, or 72
    if re.search(r'\b(8|24|72)\b', message_text):
        # Forward the new message to the target channel or bot
        await client.forward_messages(target_channel, event.message)

# Main function to start the client
async def main():
    # Start the client with forced SMS authentication
    await client.start(phone, force_sms=True)
    print(f'Monitoring new posts in {source_channel}...')
    # Keep the script running
    await client.run_until_disconnected()

# Start the client
if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
