# pip install python-telegram-bot
# pip install qdrant-client
# pip install transformers
# pip install langchain
# pip install python-dotenv
# pip install openai
# docker run -p 6333:6333 qdrant/qdrant

from flask import Flask, request, jsonify
import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
from handlers import start, handle_message

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")

@app.route('/webhook', methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(), bot)
    await application.process_update(update)
    return "ok"

if __name__ == '__main__':
    application = Application.builder().token(telegram_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()
    app.run(host='0.0.0.0', port=5000)