from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
from rest_framework import status, request
from rest_framework.response import Response


class User(AbstractBaseUser):
    username = models.CharField(max_length=32, primary_key=True)

    USERNAME_FIELD = 'username'

    def create(self, username):
        if not username:
            raise ValueError('Username is required')
        return self

    def get_user_model(self):
        return self
