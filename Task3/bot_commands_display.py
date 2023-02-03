import logger as log    
from telegram import Update
from telegram.ext import CallbackContext

async def find_contact(update: Update, context: CallbackContext):
    await log.logger('Информация о контакте, запрошенном пользователем')
    await update.message.reply_text('Введите фамилию: ')   
    text = update.message.text.split()
    surname = text[1]
    with open('Task3\phonebook.txt', 'r') as data:
        data = data.read().split('\n')
        for i in range(len(data)):
            if f'Surname: {surname}' in data[i]:
                await update.message.reply_text(f"{data[i]}'\n'{data[i+1]}'\n'{data[i+2]}'\n'{data[i+3]}")
    await log.logger('Информация о контакте')
    await log.log(update, context)

async def export_phonebook(update: Update, context: CallbackContext):
    await log.logger('Пользователь выбрал экспорт телефонной книги')
    await update.message.reply_text(f'''Выберете формат : 
        экспорт в .txt формат - нажмите /txt,
        экспорт в .csv формат - нажмите /csv,
        в сообщение - нажмите /here''')
    user_input = update.message.text
    await log.logger('Пользователь выбрал формат экспорта')
    await log.log(update, context)

async def export_phonebook_txt(update: Update, context: CallbackContext):
    await log.logger('Экспорт телефонной книги в формате .txt по запросу пользователя')
    await log.log(update, context)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('Task3/phonebook.txt', 'rb'))
    await log.logger('Телефонная книга в формате.txt выгружена')

async def export_phonebook_csv(update: Update, context: CallbackContext):
    await log.logger('Экспорт телефонной книги в формате .csv по запросу пользователя')
    await log.log(update, context)
    with open('Task3/phonebook.csv', 'w') as file:
        with open('Task3/phonebook.txt', 'r') as data:
            data = data.readlines()
            file.writelines(data)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('Task3/phonebook.csv', 'rb'))
    await log.logger('Телефонная книга в формате.csv выгружена')

async def export_phonebook_message(update: Update, context: CallbackContext):
    await log.logger('Предварительный просмотр телефонной книги по запросу пользователя')
    await log.log(update, context)
    with open('Task3\phonebook.txt', 'r') as data:
        text = '\n'.join(data.readlines())
        await update.message.reply_text(text)
   
