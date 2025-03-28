import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from styles.font_styles import generate_fancy_name, generate_bio_style, apply_style, add_decorations
from aiohttp import web
import asyncio

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

# Health check handler
async def health_check(request):
    return web.Response(text="OK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = """
🌟 Welcome to the Fancy Font Bot! 🌟

I can help you create beautiful stylized text for your Telegram bio and messages!

Commands:
/name <text> - Create fancy styled names
/bio <text> - Generate stylish bio text
/fonts - Show available font styles
/help - Show this help message

Example:
/name John Doe
/bio Living life to the fullest ✨

Let's make your text beautiful! 😊
    """
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📝 Available Commands:

/name <text> - Transform your name into fancy styles
/bio <text> - Create a stylish bio
/fonts - View all available font styles
/help - Show this help message

Tips:
• Keep text under 100 characters
• Try different styles with the same text
• Use emojis for extra flair ✨

Examples:
/name Alex
/bio Dreams ✨ Goals 🎯 Success 🌟

Need more help? Just ask! 😊
    """
    await update.message.reply_text(help_text)

async def fonts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sample_text = "Sample Text"
    styles = generate_fancy_name(sample_text)
    
    message = "Available Font Styles:\n\n"
    for style in styles:
        message += f"{style['style']}: {style['text']}\n"
    
    await update.message.reply_text(message)

async def name_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Please provide text to style!\n"
            "Example: /name John Doe"
        )
        return
    
    text = ' '.join(context.args)
    if len(text) > 100:
        await update.message.reply_text(
            "Text too long! Please keep it under 100 characters."
        )
        return
    
    try:
        styles = generate_fancy_name(text)
        keyboard = []
        
        for style in styles:
            keyboard.append([
                InlineKeyboardButton(
                    f"Copy {style['style'].title()}", 
                    callback_data=f"copy:{style['text']}"
                )
            ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Choose a style to copy:",
            reply_markup=reply_markup
        )
        
    except Exception as e:
        logger.error(f"Error in name_command: {str(e)}")
        await update.message.reply_text(
            "Sorry, there was an error processing your request. Please try again!"
        )

async def bio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Please provide text for your bio!\n"
            "Example: /bio Living my best life ✨"
        )
        return
    
    text = ' '.join(context.args)
    if len(text) > 100:
        await update.message.reply_text(
            "Text too long! Please keep it under 100 characters."
        )
        return
    
    try:
        styles = generate_bio_style(text)
        keyboard = []
        
        for i, style in enumerate(styles):
            if i % 2 == 0:
                keyboard.append([])
            keyboard[-1].append(
                InlineKeyboardButton(
                    f"Copy Style {i+1}", 
                    callback_data=f"copy:{style['text']}"
                )
            )
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Choose a bio style to copy:",
            reply_markup=reply_markup
        )
        
    except Exception as e:
        logger.error(f"Error in bio_command: {str(e)}")
        await update.message.reply_text(
            "Sorry, there was an error processing your request. Please try again!"
        )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    try:
        action, data = query.data.split(':', 1)
        
        if action == "copy":
            await query.message.reply_text(
                f"Here's your styled text:\n\n{data}\n\n"
                "✨ Just tap and hold to copy! ✨"
            )
        
    except Exception as e:
        logger.error(f"Error in button_callback: {str(e)}")
        await query.message.reply_text(
            "Sorry, there was an error processing your request. Please try again!"
        )

def main():
    # Create web application
    app = web.Application()
    app.router.add_get('/health', health_check)
    
    # Create bot application
    bot_app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("help", help_command))
    bot_app.add_handler(CommandHandler("fonts", fonts_command))
    bot_app.add_handler(CommandHandler("name", name_command))
    bot_app.add_handler(CommandHandler("bio", bio_command))
    bot_app.add_handler(CallbackQueryHandler(button_callback))
    
    # Get port from environment variable or use default
    port = int(os.getenv('PORT', 8080))
    
    # Start both web and bot
    async def start_services():
        # Start web server
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        
        # Start bot
        await bot_app.initialize()
        await bot_app.start()
        await bot_app.run_polling()
    
    # Run everything
    asyncio.run(start_services())

if __name__ == '__main__':
    main() 