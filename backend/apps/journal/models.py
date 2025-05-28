from django.db import models
from apps.users.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    mood = models.CharField(max_length=50, blank=True)  # e.g., 'happy', 'sad'
    sentiment_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title or 'Entry'} ({self.created_at.date()})"