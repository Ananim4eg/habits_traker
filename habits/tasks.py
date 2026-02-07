from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_reminder


@shared_task
def send_message_telegram():
    """Задача на отправку напоминания в телеграм"""
    habits = Habit.objects.all()

    time_now = datetime.now().strftime("%H:%M")

    for habit in habits:
        if habit.time.strftime("%H:%M") == time_now:
            send_reminder(habit.habit_name, habit.owner.telegram_id)
