from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notice(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=120, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_notices')
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='notices/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-publish_date', '-created_at']
        indexes = [
            models.Index(fields=['publish_date']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.title} ({self.publish_date.date()})"
