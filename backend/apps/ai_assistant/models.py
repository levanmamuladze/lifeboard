from django.db import models
from apps.users.models import User

class WeeklySummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weekly_summaries')
    week_start = models.DateField()
    summary_text = models.TextField()
    ai_tips = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'week_start')
        ordering = ['-week_start']

    def __str__(self):
        return f"Summary for {self.user.username} ({self.week_start})"