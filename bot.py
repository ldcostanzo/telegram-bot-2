import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Caricamento variabili ambiente
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("URL")

if not TOKEN:
    raise ValueError("Il token del bot non è stato trovato. Assicurati che il file .env sia corretto.")

# Crea l'applicazione del bot
app = Application.builder().token(TOKEN).build()

# Comandi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono il tuo bot Telegram.")
    chat_id = update.effective_message.chat_id
    print(chat_id)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ecco i comandi disponibili:\n/start - Avvia il bot\n/help - Mostra aiuto")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_message = update.message.text.lower()
    response = "Non ho capito la domanda, bro, parla potabile"
    if "ciao" in text_message:
        response = "Ciao anche a te bro"
    elif "come stai" in text_message:
        response = "Bene, grazie! Tu?"
    await update.message.reply_text(response)

# Aggiunta handler
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Avvia il bot in modalità webhook
if __name__ == "__main__":
    print("Avvio del bot...")
    app.run_webhook(
        listen="0.0.0.0",
        port=443,
        url_path=TOKEN,  # URL locale del webhook
        webhook_url=f"{URL}/{TOKEN}",  # URL pubblico del webhook
        key="/certs/key.pem",
        cert="/certs/cert.pem"
    )
    print(f"Webhook configurato su: {URL}/{TOKEN}")
