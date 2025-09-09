from django.contrib.auth.models import (AbstractUser, BaseUserManager, Group,
                                        Permission)
from django.db import models

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):

    objects = UserManager()

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.first_name
