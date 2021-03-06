# enidbot
A GhostWorld/Enid Telegram bot

## Features

- spits out Enid-tastic images and captions (for now just one command available: `/justkillme`)
- can be used as an [inline bot](https://core.telegram.org/bots/inline) via inline queries: just type `@YourBotName` into a conversation with anyone, and wait for the magic to happen!

## Local Setup

### Requirements
To run it locally, you need Python and pip installed. You'll also need the [python-telegram-bot library](https://github.com/python-telegram-bot/python-telegram-bot), which you can install by doing `pip install python-telegram-bot`.

### Create your telegram bot

Creating a bot is pretty easy using the [Telegram Documentation](https://core.telegram.org/bots#3-how-do-i-create-a-bot). Once you've done so, and you've created your token, you need to enable the inline mode for your bot (read more about it [here](https://core.telegram.org/bots/inline)). If you don't do so, the inline queries won't work!

### Config

Create a `config.py` file and add your Telegram API token to it:

```
TELEGRAM_SECRET_KEY = '269725652:AAFUfzsbHAnl_SbRnJa3aOTrctC8A3oAwME'
```

Your config will be imported directly in the main file, and it's also added to your `.gitignore` file by default (so you don't accidentally check your secret key into git).  
That's it, you're ready to go!

### Deployment

Deploying with [heroku](https://heroku.com/) is pretty straightforward. You can find the configuration for heroku on the `heroku` branch (some small changes in config need to be made in your main.py file). If you change your app's main file's name, make sure you update your Procfile accordingly. Before (or after) you deploy, you also need to set up your Config Vars accordingly — see the [heroku documentation on that](https://devcenter.heroku.com/articles/config-vars).

## Demo

If you have Telegram, you can ping [@EnidBot](https://telegram.me/EnidBot) or bring the bot into a conversation by typing `@EnidBot ` at the start of a message (the space is important!). Let yourself be amazed!
