import logger as log    
from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext):
    await log.logger('Пользователь запустил программу')
    await update.message.reply_text(f'''Выберите операцию: 
        найти контакт - введите /find,
        добавление нового контакта - введите /add,
        экспорт телефонной книги -введите /export,
        выгрузка журнала - введите /load''')
    user_input = update.message.text
    await log.logger('Пользователь выбрал операцию')
    await log.log(update, context)
    

async def add_contact(update: Update, context: CallbackContext):
    await log.logger('Добавление контакта по запросу пользователя')
    await update.message.reply_text('Введите фамилию: ')
    await update.message.reply_text('Введите имя: ')
    await update.message.reply_text('Введите номер телефона: ')
    await update.message.reply_text('Введите описание: ')
    text = update.message.text.split()
    surname = text[1]
    name = text[2]
    telephone = text[3]
    description = text[4]
    contact = 'Surname: '+surname+'\n'+'Name: '+name + '\n' + \
        'Telephone: '+telephone+'\n'+'Comment: '+description+'\n'
    with open('Task3\phonebook.txt', 'a') as file:
        file.write(f'{contact}\n')
    await update.message.reply_text(f'Контакт {contact} добавлен в телефонную книгу')
    await log.logger('Новый контакт создан')
    await log.log(update, context)
   





