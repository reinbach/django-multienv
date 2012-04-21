from django.db import models
from django.contrib.auth import User

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        env_exclude = True