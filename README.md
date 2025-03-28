# Telegram Fancy Font Bot

A Telegram bot that generates fancy font styles for text.

## Features

- Multiple font styles (Double Struck, Script, Bold, Italic, Medieval, and more)
- Easy to use commands
- Copy button for each style
- Clean and user-friendly interface

## Commands

- `/start` - Start the bot and see welcome message
- `/fancy [text]` - Generate text in different font styles
- `/styles` - Show all available font styles
- `/help` - Show help message

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/fontbot.git
cd fontbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your bot token:
```
BOT_TOKEN=your_telegram_bot_token_here
```

4. Run the bot:
```bash
python bot.py
```

## Deployment on Render

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add your `BOT_TOKEN` as an environment variable
5. Deploy!

## License

MIT License 