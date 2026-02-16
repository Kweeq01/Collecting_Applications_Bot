from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards import main_kb
from aiogram.fsm.context import FSMContext
from states import GetData
import csv
import os
from dotenv import load_dotenv
import phonenumbers
from phonenumbers import NumberParseException
from datetime import datetime

router = Router()

load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

if not ADMIN_ID:
    raise ValueError("ADMIN_ID not set in .env")

ADMIN_ID = int(ADMIN_ID)

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}\nSelect an action", reply_markup=main_kb)

@router.message(F.text == "Submit your application")
async def get_name(message: types.Message, state: FSMContext):
    await message.answer("Enter your name")
    await state.set_state(GetData.name)

@router.message(GetData.name)
async def get_phone(message: types.Message, state: FSMContext):
    if not message.text or not message.text.strip():
        await message.answer("The field cannot be empty. Please enter the data again.")
        return

    await state.update_data(name=message.text.strip())
    await message.answer("Enter your phone number")
    await state.set_state(GetData.phone_number)

@router.message(GetData.phone_number)
async def get_comment(message: types.Message, state: FSMContext):
    if not message.text or not message.text.strip():
        await message.answer("The field cannot be empty. Please enter the data again.")
        return

    phone_text = message.text.strip()

    try:
        phone_number = phonenumbers.parse(phone_text, "RU")

        if not phonenumbers.is_valid_number(phone_number):
            await message.answer("Enter the correct phone number.")
            return

    except NumberParseException:
        await message.answer("Enter the number in the format +79991234567")
        return

    formatted_phone = phonenumbers.format_number(
        phone_number,
        phonenumbers.PhoneNumberFormat.E164
    )

    await state.update_data(phone=formatted_phone)
    await message.answer("Enter your comment")
    await state.set_state(GetData.comment)

@router.message(GetData.comment)
async def save_data(message: types.Message, state: FSMContext):
    if not message.text or not message.text.strip():
        await message.answer("The field cannot be empty. Please enter the data again.")
        return

    await state.update_data(comment=message.text.strip())
    data = await state.get_data()

    try:
        save_to_csv(data)
    except Exception as e:
        await message.answer("Error saving data.")
        print(e)
        return

    text = (
        f"📩 New application:\n\n"
        f"Name: {data['name']}\n"
        f"Phone: {data['phone']}\n"
        f"Comment: {data['comment']}"
    )

    await message.bot.send_message(ADMIN_ID, text)

    await message.answer("Thanks! Your application has been saved")
    await state.clear()

def save_to_csv(data: dict, filename="user_data.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["name", "phone", "comment", "date"])

        writer.writerow([
            data.get("name"),
            data.get("phone"),
            data.get("comment"),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])
