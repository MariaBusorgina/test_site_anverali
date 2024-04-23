## Разработка сайта с админ-панелью и кабинетами заказчика и исполнителя. 

Проект создан с использованием Django и базы данных PostgreSQL.

#### Установка

1. Клонировать репозиторий  
```bash
git clone https://github.com/MariaBusorgina/test_site_anverali.git
```
2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate
```
3. Перейти в каталог
```bash
cd works
```
4. Установить зависимости
```bash
pip install -r requirements.txt
```
5. Настройка переменных окружения  
Создайте файл .env в корневой директории проекта и добавьте в него следующие переменные:  
```bash
DB_NAME=название_базы_данных
DB_USER=пользователь_базы_данных
DB_PASSWORD=пароль_базы_данных
SECRET_KEY=ваш_секретный_ключ
```
6. Создать и применить миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
8. Создать администратора 
```bash
python manage.py createsuperuser
```
9. Запуск сервера
```bash
python manage.py runserver
```

[Административная панель](http://127.0.0.1:8000/admin/) - доступ к административной панели приложения.

