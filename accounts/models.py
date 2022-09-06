from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now
import datetime


def get_exp_time():
    current_timestamp = datetime.datetime.now().timestamp()
    exp = int(current_timestamp) + 3600
    return str(exp)


def update_last_login(user):
    user.last_login = now()
    user.save()


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, username, password, **extra_fields)

    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=30, unique=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return "%s %s" % (self.email, self.username)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = '유저 목록'
