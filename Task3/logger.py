from datetime import datetime as dt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def logger(text):
    with open('Task3\log.txt', 'a') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        data.write(time +' ' + str(text)+'\n')

async def log(update: Update, context: CallbackContext):
    file = open('Task3\log.txt', 'a')
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    file.write(f'{time} {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()


async def export_logging_journal(update: Update, context: CallbackContext):
    await logger('User chose export of the logging journal')
    await update.message.reply_text(f'''Choose a format: 
        export in .txt format - enter /intxt,
        in message - enter /inmessage''')
    user_input = update.message.text
    await logger('User chose an export format')
    await log(update, context)

async def export_logging_journal_txt(update: Update, context: CallbackContext):
    await logger('Экспорт журнала регистрации в формате .txt по запросу пользователя')
    await log(update, context)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('Task3/log.txt', 'rb'))
    await logger('log.txt unloaded')

async def export_logging_journal_message(update: Update, context: CallbackContext):
    await log(update, context)
    await logger('Предварительный просмотр журнала регистрации, запрошенный пользователем')
    with open('Task3\log.txt', 'r') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        text = time + '\n'.join(data.readlines())
        await update.message.reply_text(text)

