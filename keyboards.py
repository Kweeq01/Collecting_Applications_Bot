from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Submit your application")]
    ],
    resize_keyboard=True
)