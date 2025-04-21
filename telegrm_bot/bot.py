import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import datetime

API_TOKEN = '7897527451:AAFk7JrUQ1yQz-bpVg-lByN7l8_KsVweF2M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Путь к папке для анкет
folder_path = "ankety"

# Проверка, существует ли папка, если нет — создаем её
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Я бот для анкет.\n"
        "Вакансии:\n"
        "- Подсобник (500 грн/день, выплаты каждую субботу)\n"
        "- Офис\n"
        "Напиши 'Да', чтобы начать анкету."
    )

@dp.message(F.text.lower() == "да")
async def form_handler(message: Message):
    await message.answer(
        "Отправь анкету в одном сообщении:\n"
        "1. Имя\n"
        "2. Возраст\n"
        "3. Опыт работы\n"
        "4. Где живёшь\n"
        "5. Мешает ли работа учёбе?\n"
        "6. Когда готов приступить\n"
        "7. Оставьте свои контакты (телеграм или номер)"
    )

@dp.message()
async def after_form_handler(message: Message):
    # Сохранение анкеты в файл
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    form_data = message.text
    
    # Создание пути к файлу с анкетами
    file_path = os.path.join(folder_path, "ankety.txt")
    
    # Запись анкеты в файл
    with open(file_path, "a") as file:
        file.write(f"Дата: {now}\nАнкета:\n{form_data}\n\n")
    
    await message.answer("Спасибо! Мы получили анкету и свяжемся с тобой.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())