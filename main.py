from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Функция, которая будет обрабатывать команды /start и /help
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который повторяет все, что ты скажешь.')


# Функция, которая будет повторять сообщения
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


# Основная функция для запуска бота
def main():
    # Вставьте сюда ваш токен, который вы получили от BotFather
    token = '***REMOVED***'

    # Создаем экземпляр класса Updater и передаем ему токен
    updater = Updater(token)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команд /start и /help
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик всех текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Работаем до прерывания
    updater.idle()


if __name__ == '__main__':
    main()
