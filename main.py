from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    user_id = user.id
    username = user.username if user.username else 'No username'
    first_name = user.first_name if user.first_name else 'No first name'
    last_name = user.last_name if user.last_name else 'No last name'

    save_user_info(user_id, username, first_name, last_name)
    await update.message.reply_text(f'Привет, {first_name}! Я переписываю твои сообщения ЗаБоРоМ.')


def save_user_info(user_id: int, username: str, first_name: str, last_name: str):
    with open("user_info.txt", "a", encoding='utf-8') as file:
        file.write(f"ID: {user_id}, Username: {username}, First Name: {first_name}, Last Name: {last_name}\n")


def save_message(user_id: int, username: str, first_name: str, last_name: str, message: str):
    with open("messages.txt", "a", encoding='utf-8') as file:
        file.write(f"ID: {user_id}, Username: {username}, First Name: {first_name}, Last Name: {last_name}, Message: {message}\n")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    original_text = update.message.text
    transformed_text = transform_text(original_text)

    user = update.message.from_user
    user_id = user.id
    username = user.username if user.username else 'No username'
    first_name = user.first_name if user.first_name else 'No first name'
    last_name = user.last_name if user.last_name else 'No last name'

    save_message(user_id, username, first_name, last_name, transformed_text)

    await update.message.reply_text(transformed_text)
    await context.bot.send_message(chat_id="367311863", text=f'#NewMessage:\nID: {user_id}, Username: {username}, First Name: {first_name}, Last Name: {last_name}, Message: {transformed_text}')



def transform_text(text: str) -> str:
    result = []
    toggle = True
    for char in text:
        if char.isalpha():
            if toggle:
                result.append(char.upper())
            else:
                result.append(char.lower())
            toggle = not toggle
        else:
            result.append(char)
    return ''.join(result)


def main():
    token = TOKEN
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == '__main__':
    main()
