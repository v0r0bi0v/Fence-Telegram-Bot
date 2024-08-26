from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


# Функция, которая будет обрабатывать команды /start и /help
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, который повторяет все, что ты скажешь.')


# Функция, которая будет повторять сообщения
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


# Основная функция для запуска бота
def main():
    # Вставьте сюда ваш токен, который вы получили от BotFather
    token = 'YOUR_TOKEN_HERE'

    # Создаем экземпляр класса Application и передаем ему токен
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команд /start и /help
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()
