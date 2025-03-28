from typing import List, Dict, Any
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import asyncio

def setup_logging():
    """Configure logging for the bot."""
    logging.basicConfig(
        filename='bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger(__name__)

def safe_execute(func):
    """Decorator for safely executing functions with error handling."""
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

def create_inline_keyboard(buttons: List[Dict[str, str]], columns: int = 2) -> InlineKeyboardMarkup:
    """Create an inline keyboard with the specified buttons and column layout."""
    keyboard = []
    row = []
    
    for button in buttons:
        if len(row) >= columns:
            keyboard.append(row)
            row = []
        row.append(InlineKeyboardButton(text=button['text'], callback_data=button['callback_data']))
    
    if row:
        keyboard.append(row)
    
    return InlineKeyboardMarkup(keyboard)

def format_error_message(error: Exception) -> str:
    return f"An error occurred: {str(error)}"

def validate_text(text: str, max_length: int = 100) -> bool:
    """Validate text length and content."""
    return bool(text and len(text) <= max_length)

async def rate_limit(user_id: int, context: Dict[str, Any], limit: int = 5, window: int = 60):
    current_time = asyncio.get_event_loop().time()
    
    if user_id not in context:
        context[user_id] = []
        
    # Remove old timestamps
    context[user_id] = [t for t in context[user_id] if current_time - t < window]
    
    if len(context[user_id]) >= limit:
        return False
        
    context[user_id].append(current_time)
    return True 