# Fancy Font Telegram Bot

A Telegram bot that generates fancy text styles and beautiful bios with special characters and decorations.

## Features

- Multiple font styles (Normal, Bold, Italic, Fancy)
- Decorative elements (Stars, Hearts, Flowers, etc.)
- Bio styling with various combinations
- Easy to use commands
- Copy button functionality
- Beautiful formatting

## Commands

- `/start` - Start the bot and see welcome message
- `/help` - Show help and usage instructions
- `/name <text>` - Create fancy styled names
- `/bio <text>` - Generate stylish bio text
- `/fonts` - Show available font styles

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

3. Set up environment variables:
Create a `.env` file with:
```
BOT_TOKEN=your_telegram_bot_token
```

4. Run the bot:
```bash
python bot.py
```

## Deployment on Render

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add environment variable:
   - Key: `BOT_TOKEN`
   - Value: Your Telegram bot token
5. Deploy!

## Usage Examples

1. Create a fancy name:
```
/name John Doe
```

2. Create a stylish bio:
```
/bio Living my best life ✨
```

3. View available fonts:
```
/fonts
```

## License

MIT License - feel free to use and modify! 