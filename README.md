# TeleParse

A script to parse through messages sent and received in a Telegram account and archive them to an excel file based on keyword.

Utilizes the [Telethon](https://github.com/LonamiWebs/Telethon) library for a straightforward way to use [Telegram](https://telegram.org/)'s own API

## How to use

If running the script directly:

```
pip install requirements.txt
```

Currently the Telegram api id and hash are stored in environment variables for safety reasons so may not work. You will need your own id and hash to put in your dotenv file.

The first time you run the script, it will ask for the number (or bot token if you are developing a bot program) you use for Telegram. Follow the format found in your Telegram account: +1 (123) 456-7890

Afterwards, the program will ask for a keyword and type in the desired word to search for.