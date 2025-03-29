from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Caricamento variabili ambiente
load_dotenv()
TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = os.getenv('BOT_USER')
URL = os.getenv("URL")

async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Laura i\'m your test bot')

async def help_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Mi scoccio di scrivere l help ')

async def custom_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Inserisci il comando custom')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'ciao' in processed:
        return 'ciao'

    if 'come stai' in processed:
        return 'bene grazie, tu?'

    return 'Bro'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group' or message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot',response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Start bot')
    app =  Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)
    
    print('Start Polling')
    app.run_polling(poll_interval=3)

#  Avvia il bot in modalità webhook

#    app.run_webhook(
#         listen="0.0.0.0",
#         port=443,
#         url_path=TOKEN,  # URL locale del webhook
#         webhook_url=f"{URL}/{TOKEN}",  # URL pubblico del webhook
#         key="/certs/key.pem",
#         cert="/certs/cert.pem"
#         )  
# print(f"Webhook configurato su: {URL}/{TOKEN}")
