from datetime import datetime as dt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext


async def logger(text):
    with open('Task2\log.txt', 'a') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        data.write(time +' ' + str(text)+'\n')

async def log(update: Update, context: CallbackContext):
    file = open('Task2\log.txt', 'a')
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    file.write(f'{time} {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

async def logger_journal(update: Update, context: CallbackContext):
    log(update, context)
    logger('Предварительный просмотр журнала')
    with open('Task2\log.txt', 'r') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        text = time + '\n'.join(data.readlines())
        await update.message.reply_text(text)


