from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, )
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()

    def __str__(self):
        return str(self.user)
