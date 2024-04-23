from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    """Форма для регистрации пользователя"""
    ROLE_CHOICES = (
        ('customer', 'Заказчик'),
        ('executor', 'Исполнитель'),
    )
    role = forms.ChoiceField(label='Выберите', choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'role', 'contact', 'experience']


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для авторизации пользователя"""

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

