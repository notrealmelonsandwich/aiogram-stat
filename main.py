import csv
import datetime
import pymysql

from aiogram import Bot, Dispatcher, executor
from aiogram import types
import aiogram.utils.markdown as md

API_TOKEN = ''

SQL_DATABASE_ADDRESS = '127.0.0.1'
SQL_USERNAME = 'bot'
SQL_PASSWORD = 'bot'
SQL_DATABASE_NAME = 'bot'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет")
    statistics(message.chat.id, message.text)
    stat(message, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)


def statistics(user_id, command):
    date = datetime.datetime.today().strftime("%d-$m-%Y %H:%M")
    with open('data.csv', 'a', newline='') as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([date, user_id, command])


def stat(user_id, command):
    connection = pymysql.connect(SQL_DATABASE_ADDRESS, SQL_USERNAME, SQL_PASSWORD, SQL_DATABASE_NAME)
    cursor = connection.cursor()
    date = datetime.datetime.today().strftime("%d-$m-%Y %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '%s', '%s'" % (user_id, command, date))
    connection.commit()
    cursor.close()