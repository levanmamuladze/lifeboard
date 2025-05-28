from django.db import models
from apps.users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)  # e.g., 'daily', 'weekly'
    streak = models.PositiveIntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)
    reminder_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name