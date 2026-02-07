from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    fields = ("__all__",)
