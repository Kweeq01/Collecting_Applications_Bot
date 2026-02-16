# Telegram Application Bot

## 🇬🇧 English

### 📌 Description
This project is a Telegram bot built with **aiogram 3**.  
The bot collects applications from users and sends them to an administrator.

### 🚀 Features
- Greets the user
- Provides a "Submit your application" button
- Sequentially requests:
  - Name
  - Phone number (validated using `phonenumbers`)
  - Comment
- Saves applications to a CSV file
- Sends confirmation to the user
- Forwards the application to the administrator

---

### 🛠 Technologies Used
- Python 3.10+
- aiogram 3
- FSM (Finite State Machine)
- phonenumbers (phone validation)
- python-dotenv
- CSV file storage

---

### 📂 Project Structure
```
.
├── main.py
├── handlers.py
├── states.py
├── keyboards.py
├── .env
└── README.md
```

---

### ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Kweeq01/Collecting_Applications_Bot.git
cd Collecting_Applications_Bot
```

2. Install dependencies:

`pip install aiogram phonenumbers python-dotenv`

3. Create a .env file in the root directory:

```python
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_id_here
```

---

### 🔑 How to Get ADMIN_ID

1. Temporarily add a handler:

```python
@router.message(Command("id"))
async def get_id(message: types.Message):
    await message.answer(f"Your ID: {message.from_user.id}")
```

2. Run the bot

3. Send /id

4. Copy your Telegram ID into .env

---

### ▶️ Running the Bot
`python main.py`

---

### 📁 Data Storage

All applications are stored in:

`user_data.csv`

Format:
```
name, phone, comment, date
```

---

### 📌 Notes

- Phone numbers are validated and formatted to E.164 standard.

- FSM is used to track user input steps.

- The bot uses MemoryStorage for state management.

- Applications are automatically forwarded to the admin.

---

## 🇷🇺 Русская версия
### 📌 Описание

Проект представляет собой Telegram-бота на aiogram 3.
Бот собирает заявки от пользователей и отправляет их администратору.

### 🚀 Возможности

- Приветствует пользователя

- Предлагает кнопку "Submit your application"

- Последовательно запрашивает:

  - Имя
  - Номер телефона (с проверкой через phonenumbers)
  - Комментарий

- Сохраняет заявки в CSV-файл

- Отправляет подтверждение пользователю

- Пересылает заявку администратору

---

### 🛠 Используемые технологии

- Python 3.10+

- aiogram 3

- FSM (конечный автомат состояний)

- phonenumbers (проверка телефона)

- python-dotenv

- Хранение данных в CSV

---

### 📂 Структура проекта
```
.
├── main.py
├── handlers.py
├── states.py
├── keyboards.py
├── .env
└── README.md
```

---

### ⚙️ Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/Kweeq01/Collecting_Applications_Bot.git
cd Collecting_Applications_Bot
```

2. Установить зависимости:

`pip install aiogram phonenumbers python-dotenv`

3. Создать файл .env в корне проекта:

```python
BOT_TOKEN=ваш_токен_бота
ADMIN_ID=ваш_telegram_id
```

---

### 🔑 Как узнать ADMIN_ID

1. Временно добавить обработчик:

```python
@router.message(Command("id"))
async def get_id(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")
```

2. Запустить бота

3. Отправить /id

4. Вставить полученный ID в .env

---

### ▶️ Запуск бота
`python main.py`

---

### 📁 Хранение данных

Все заявки сохраняются в файл:

`user_data.csv`

Формат:

`name, phone, comment, date`

---

### 📌 Примечания

- Номера телефонов валидируются и сохраняются в международном формате E.164.

- Для отслеживания шагов используется FSM.

- Используется MemoryStorage для хранения состояний.

- Все заявки автоматически пересылаются администратору.
