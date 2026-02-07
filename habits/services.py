import requests

from config import settings


def send_reminder(habit_name, telegram_id):
    """Функция для отправки напоминаний в телеграм"""

    url = f'{settings.TELEGRAM_API_URL}{settings.TELEGRAM_API_BOT}/sendMessage'

    params ={
        'text': f'Напоминание!!! \nПора выполнить {habit_name}',
        'chat_id': telegram_id
    }

    requests.get(url, params=params)
    send_reminder('123', 483927133)