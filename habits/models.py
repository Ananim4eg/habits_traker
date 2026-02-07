from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class Habit(models.Model):
    """Модель привычек"""

    habit_name = models.CharField(
        max_length=50,
        verbose_name='Название привычки'
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="habits",
        verbose_name='Создатель привычки'
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения привычки'
    )
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name='Время для выполнения привычки'
    )
    action = models.CharField(
        max_length=50,
        verbose_name='Действие'
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name='Признак полезной привычки'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='linked_as_related',
        verbose_name='Связанная привычка'
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Периодичность выполнения'
    )
    reward = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Вознаграждение'
    )
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name='Время на выполнение привычки'
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Признак публичной привычки'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f'{self.habit_name}'

    class Meta:
        ordering = ["-created_at"]

    def clean(self):

        if self.reward and self.related_habit:
            raise ValidationError("Нельзя одновременно указывать reward и related_habit.")


        if self.time_to_complete > 120:
            raise ValidationError("time_to_complete должен быть не больше 120 секунд.")


        if not (1 <= self.periodicity <= 7):
            raise ValidationError("periodicity должна быть в диапазоне 1..7 дней.")


        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("У приятной привычки не может быть reward или related_habit.")


        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("related_habit должна быть приятной привычкой.")
