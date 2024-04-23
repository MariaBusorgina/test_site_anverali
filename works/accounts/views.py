from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, CustomAuthenticationForm
from django.contrib import messages

from .models import CustomerProfile, PerformerProfile


def home(request):
    """
    Представление для отображения главной страницы сайта
    """
    return render(request, 'accounts/index.html')


def register_user(request):
    """
    Представление для регистрации пользователя с автоматической авторизацией
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()

            role = form.cleaned_data['role']

            if role == 'customer':
                CustomerProfile.objects.create(user=user)
                messages.success(request, 'Вы успешно зарегистрировались как заказчик!')
                login(request, user)
                return redirect('customer')

            elif role == 'executor':
                PerformerProfile.objects.create(user=user)
                messages.success(request, 'Вы успешно зарегистрировались как исполнитель!')
                login(request, user)
                return redirect('executor')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def login_user(request):
    """
    Представление для авторизации пользователя
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'customer':
                    return redirect('customer')
                elif user.role == 'executor':
                    return redirect('executor')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required()
def executor(request):
    """
    Представление для перехода на страницу исполнителей
    Доступно для авторизованных пользователей
    """
    if request.user.role != 'executor':
        message = 'Для доступа к этой странице вам необходимо зарегистрироваться как исполнитель.'
        return render(request, 'accounts/registration_notice.html', {'message': message})
    return render(request, 'accounts/executor_page.html')


@login_required()
def customer(request):
    """
    Представление для перехода на страницу заказчиков
    Доступно для авторизованных пользователей
    """
    if request.user.role != 'customer':
        message = 'Для доступа к этой странице вам необходимо зарегистрироваться как заказчик.'
        return render(request, 'accounts/registration_notice.html', {'message': message})

    return render(request, 'accounts/customer_page.html')


def logout_user(request):
    """
    Выход пользователя из системы.
    Перенаправляет на страницу входа
    """
    logout(request)
    return redirect('login')


