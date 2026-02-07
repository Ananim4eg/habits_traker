import requests

from config import settings


def send_reminder(habit_name: str, telegram_id: int) -> None:
    """Функция для отправки напоминаний в телеграм"""

    url = f'{settings.TELEGRAM_API_URL}{settings.TELEGRAM_API_BOT}/sendMessage'

    params ={
        'text': f'Напоминание!!! \nПора выполнить {habit_name}',
        'chat_id': telegram_id
    }

    response = requests.get(url, params=params)
