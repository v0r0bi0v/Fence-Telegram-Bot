from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я переписываю твои сообщения ЗаБоРоМ.')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    original_text = update.message.text
    transformed_text = transform_text(original_text)
    await update.message.reply_text(transformed_text)


def transform_text(text: str) -> str:
    result = []
    toggle = False
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
    token = '***REMOVED***'

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()


if __name__ == '__main__':
    main()
