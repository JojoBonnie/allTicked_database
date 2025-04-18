from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add custom fields here if needed
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
