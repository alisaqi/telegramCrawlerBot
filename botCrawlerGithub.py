#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from datetime import time, datetime
import asyncio
import time as tm

channelsDictionary = {
    'A': -1000000000000,
    'B': -1000000000000,
    'C': -1000000000000,
}
# Depending on the destination chat, you can either enter the Chat ID or the username of the chat.
myBotID = {
    'Destination Chat': 'XXXXXXXXXX'
}

# the name of session file has to be a string.
# api_id has to be a integer.
# api_hash has to be a string.

app = Client("XXXXXX",
             api_id=XXXXXXX,
             api_hash="XXXXXXX"
             )


# only messages of channels will be processed by this filter. Also, since every edit of a message is an event as
# well, this filter prevenet edited messages to be processed by the code.

@app.on_message(filters.channel & ~filters.edited)
def channels(app, message: Message):
    """
    this function crawl all channels that are listed below, and sends the messages to the specified bot
    :param app: is the client of the userBot
    :param message: is the object of a message
    """
    try:

        # You can set a time for your bot to be run only in those hours
        if time(4, 29, 58) < datetime.now().time() < time(20, 0, 0):

            if message.sender_chat.id == channelsDictionary['A']:
                tm.sleep(5)
                app.forward_messages(chat_id=myBotID['Destination Chat'], from_chat_id=channelsDictionary['A'],
                                     message_ids=message.message_id)

            elif message.sender_chat.id == channelsDictionary['B']:
                tm.sleep(5)
                app.forward_messages(chat_id=myBotID['Destination Chat'], from_chat_id=channelsDictionary['B'],
                                     message_ids=message.message_id)

            elif message.sender_chat.id == channelsDictionary['C']:
                tm.sleep(5)
                app.forward_messages(chat_id=myBotID['Destination Chat'], from_chat_id=channelsDictionary['C'],
                                     message_ids=message.message_id)

        else:
            pass
    except FloodWait as e:
        asyncio.sleep(e.x)  # Wait "x" seconds before continuing


app.run()
