Данные команды для Git_bash консоли
### Первое приложение ###
1) python --version - убедился что установлен пайтон
2) pip -- version - убедился что установлен менеджер пакетов pip
3) mkdir project_108 - создал папку в которой будет находится проект
4) cd project_108 - переместился в эту папку
5) python -m venv .venv - создал виртуальную среду
6) source .venv/Scripts/activate.bat - активация виртуальной среды
7) python -m pip install Django - установка джанго
8) django-admin startproject edutest - создаю проект джанго под именем edutest
9) cd edutest - переход в созданную папку с проектом
10) python manage.py runserver - запускаем сервер для проверки
11) ctrl + с  - останавливаем сервер
12) python manage.py startapp edutest_app - создаю приложение edutest_app
13) cd edutest - перехожу в папку где хронится файл с настройками
14) nano settings.py - открываю блокнот и вношу изменнения в файл, добавляя в переменную INSTALLED_APPS название созданного до этого приложения "edutest_app"
```python
settings.py
________________________
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-j8f2*)#din5$_dcj7eo)1yncx=gbbq+(6il316$cv)i2dfa^2="

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "edutest_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "edutest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "edutest.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

```
15) cd .. - возвращаюсь назад в основную папку проекта
16) cd edutest_app  - перехожу в папку с приложением
17) nano views.py  - открываем файл куда пишем код страницы
```python
views.py
________________________
from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Hello world")
```
18) cd .. - назад в каталог проекта
19) cd edutest - перехожу в папку с настройками проекта
20) nano urls.py  - редактируем код для отображения приложения
```python
urls.py
________________________
from django.contrib import admin
from django.urls import path
 
urlpatterns = [
    path('admin/', admin.site.urls),
]
```
21) cd .. - вернулся в основную папку проекта, где распологается manage.py
22) python manage.py runserver - запускаем сервер и смотрим изменения
23) ctrl + с - останавливаем сервер
24) deactivate - диактивируем виртуальной среды
### Шаблоны ###
