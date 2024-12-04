from telegram import Update
from telegram.ext import CallbackContext
from langchain_utils import get_response
from qdrant_utils import get_embedding, store_embedding

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola soy un bot creado por Enmanuel, puedes hacerme preguntas')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    embedding = get_embedding(user_input)
    store_embedding(user_input, embedding)
    response = get_response(user_input)
    await update.message.reply_text(response)