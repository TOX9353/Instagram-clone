from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['nickname_id']

    def __str__(self):
        return self.nickname_id

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "User"
