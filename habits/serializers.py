from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычек"""
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = ['id', 'owner', 'habit_name', 'place', 'time', 'action', 'is_pleasant', 'periodicity', 'reward',
                  'is_public', 'time_to_complete', 'created_at']