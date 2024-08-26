from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


# Функция, которая будет обрабатывать команды /start и /help
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я переписываю твои сообщения ЗаБоРоМ.')


# Функция, которая будет преобразовывать текст сообщения
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    original_text = update.message.text
    transformed_text = transform_text(original_text)
    await update.message.reply_text(transformed_text)


def transform_text(text: str) -> str:
    result = []
    toggle = False  # Параметр для чередования регистра
    for char in text:
        if char.isalpha():
            if toggle:
                result.append(char.upper())
            else:
                result.append(char.lower())
            toggle = not toggle
        else:
            result.append(char)  # Не изменяем не буквенные символы

    return ''.join(result)


# Основная функция для запуска бота
def main():
    # Вставьте сюда ваш токен, который вы получили от BotFather
    token = '***REMOVED***'

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
