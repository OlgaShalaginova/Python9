# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

import logger as log
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import user_interface as ui

app = ApplicationBuilder().token("Ваш Токен").build()
print('Старт')
     
app.add_handler(CommandHandler("start", ui.start))
app.add_handler(CommandHandler("get", ui.get_data))
app.add_handler(CommandHandler("load", log.logger_journal))
app.run_polling()









