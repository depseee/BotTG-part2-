from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/MyboxRollsBot')

#@dp.message_handler(commands=['Режим_работы'])
async def rolls_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Каждый день с 10:00 до 22:00')

#@dp.message_handler(commands=['Расположение'])
async def rolls_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Фрунзе 180Д')

@dp.message_handler(commands=['Меню'])
async def rolls_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(rolls_open_command, commands=['Режим_работы'])
	dp.register_message_handler(rolls_place_command, commands=['Расположение'])
	dp.register_message_handler(rolls_menu_command, commands=['Меню'])