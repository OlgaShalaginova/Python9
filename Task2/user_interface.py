import logger as log    
from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def start(update: Update, context: CallbackContext):
    await log.logger('Запуск программы')
    await update.message.reply_text(f'Выберете операцию: расчет - введите /get, просмотр журнала - введите /load')
    await log.logger('Пользователь выбрал операцию')
    user_input = update.message.text


async def get_data(update: Update, context: CallbackContext):
    await update.message.reply_text('Введите номер 1:')
    await update.message.reply_text('Введите оператор:')
    await update.message.reply_text('Введите номер 2:')
    text = update.message.text.split()
    a = text[1]
    op = text[2]
    b = text[3]
    await log.logger(f'Введеные пользователем данные')
    await log.log(update, context)

    if 'j' in a:
        a = complex(a)
    if 'j' in b:
        b = complex(b)
    else:
        a = int(a)
        b = int(b)

    result = 0
    await log.logger(f'Расчет {a} {op} {b}')
    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    await update.message.reply_text(f'Результат = {result}')
    await log.logger(f'Результат показан пользователю {result}')




