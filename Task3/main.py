# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import bot_commands_enter as bce
import bot_commands_display as bcd

import logger as log
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

import os
import random
os.system('cls')

app = ApplicationBuilder().token("Токен").build()
print('Старт')

app.add_handler(CommandHandler("start", bce.start))
app.add_handler(CommandHandler("add", bce.add_contact))
app.add_handler(CommandHandler("find", bcd.find_contact))

app.add_handler(CommandHandler("export", bcd.export_phonebook))
app.add_handler(CommandHandler("txt", bcd.export_phonebook_txt))
app.add_handler(CommandHandler("csv", bcd.export_phonebook_csv))
app.add_handler(CommandHandler("here", bcd.export_phonebook_message))

app.add_handler(CommandHandler("load", log.export_logging_journal))
app.add_handler(CommandHandler("intxt", log.export_logging_journal_txt))
app.add_handler(CommandHandler("inmessage", log.export_logging_journal_message))

app.run_polling()







    



# elif user_input == '3':
#     print('Choose a view format: HTML - 1, CSV.file - 2, terminal - 3')
#     next_input = c.check_input_3()

#     if next_input == '1':
#         hp.create_html()
#     elif next_input == '2':
#         cp.create_csv()
#     else:
#         print(*(dd.show_phonebook()))

# else:
#     print('Choose a view format: CSV.file - 1, terminal - 2')
#     next_input = c.check_input_2()
#     if next_input == '1':
#         log.log_output_data_csv()
#     else:
#         log.log_output_data_term()
