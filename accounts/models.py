from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    picture = models.TextField(null=True, blank=True)

    # bio = models.TextField(null=True, blank=True)
