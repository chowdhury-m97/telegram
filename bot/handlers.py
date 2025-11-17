from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Say hi 👋", callback_data="hi")],
        [InlineKeyboardButton("Help ❓", callback_data="help")],
    ]
    if update.message:
        await update.message.reply_text(
            "Hey! I’m a Django-powered Telegram bot. Try a message or press a button:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Commands:\n/start\n/help\n/ping")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("pong 🏓")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(f"You said: {update.message.text}")

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "hi":
        await query.edit_message_text("Hi there! 👋")
    elif query.data == "help":
        await query.edit_message_text("Try /help for commands or send me a message.")

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
