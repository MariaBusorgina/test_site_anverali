from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError("Введите почту пользователя")
        if not first_name:
            raise ValueError("Введите имя пользователя")
        if not last_name:
            raise ValueError("Введите фамилию пользователя")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Заказчик'),
        ('executor', 'Исполнитель'),
    )
    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES)
    contact = models.CharField('Контактные данные', max_length=100)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Почта', max_length=255, unique=True)
    experience = models.CharField('Опыт', max_length=255, blank=True, null=True)

    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')

    class Meta:
        verbose_name = "Профиль заказчика"
        verbose_name_plural = "Профили заказчиков"


class PerformerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='performer_profile')

    class Meta:
        verbose_name = "Профиль исполнителя"
        verbose_name_plural = "Профили исполнителей"




