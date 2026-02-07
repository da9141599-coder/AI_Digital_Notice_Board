from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Ensure every User has a Profile.
    - When a new user is created, create a profile.
    - For existing users (like 'darshan') who might not have a profile yet,
      create one if missing.
    """
    from .models import Profile  # if needed, or remove if already imported at top

    # Always make sure a profile exists
    Profile.objects.get_or_create(user=instance)
