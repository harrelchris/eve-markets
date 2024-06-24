from django.contrib.auth.models import AbstractUser
from django.db import models

from sso.models import Token


class User(AbstractUser):
    token = models.ForeignKey(Token, on_delete=models.SET_NULL, null=True)
