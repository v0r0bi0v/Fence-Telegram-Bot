#!/bin/bash

# Переходим в директорию проекта
cd ~/projects/Fence-Telegram-Bot || exit

# Функция для запуска бота
start_bot() {
    if pgrep -f "python3 main.py --bot fence" > /dev/null; then
        echo "Fence-бот уже запущен."
    else
        nohup python3 main.py --bot fence > fence_bot.log 2>&1 &
        echo "Fence-бот запущен."
    fi
}

# Останавливаем все процессы Fence-бота
stop_all() {
    pkill -f "python3 main.py --bot fence"
    echo "Все процессы Fence-бота остановлены."
}

# Проверяем аргументы командной строки
case "$1" in
    start)
        start_bot
        ;;
    stop)
        stop_all
        ;;
    *)
        echo "Использование: $0 {start|stop}"
        exit 1
        ;;
esac

exit 0
