# Telegram Crawler Bot
Using this user bot, you can crawl all the channels in the code and forward those messages to your specified destination.

# Description

We need to create a regular Telegram account first, and then we connect to the account as a new session. By doing this, we will be able to automate processes, such as forwarding or crawling messages that we receive in our chat. Therefore we need first create an account and then use the details of this account to get `api_id` and `api_hash` from the telegram website. These two keys will allow us to create a client and connect to the account.

## Requirements 

First of all, you need to install packages that are used in this code. Since version 2.0 of pyrogram package has been published, you should only install version 1.4.8.
To install packages, use this command :

```
pip install -r requirements.txt
```
## Packages to be imported

We need to import these packages before deploying our user bot.

```
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from datetime import time, datetime
import asyncio
import time as tm
import logging
```

Every message in a chat is an event. This means that this client is like a listener and when a message is received by our account, the `@app.on_message` function will perform the action written. As an example, in this file, whenever a message is received, the `channels` function will forward it to a specific `chat_id` (each chat has its own unique ID). You can now write something else here, such as checking the sender of the message and printing a sentence if the sender is the user `A`.

As an additional note, it should be noted that in the `channelsDictionary` we store the chat IDs of the channels to which our listeners should forward their messages. In this case, the specified chat is another bot, which is called `firsteditbot`. For example, if a new message is sent to channel A, it will be transmitted immediately to `firsteditbot` chat.

Also, to prevent too many messages from being sent to the bot, we set a `FloodWait `exception which pauses it for `x` seconds.

## Run the script

To run the script you only need to run the file by command below:

```
python botCrawler.py
```

This code will create a `.session` file which stores all the parameters needed to connect to your account session without requiring any other permission. As a result, after running the file, it will ask you to enter the phone number of the account. In the next step, it will ask you to enter the code sent by telegram to confirm your session connection. In further usage, there will be no need for these steps.

## api-hash and api_id

You can get your `api-hash` and `api-id` by logging into your account at `https://my.telegram.org/auth` and then creating a new application. Upon completing the form, you will receive your account `api-id` and `api-hash`.
