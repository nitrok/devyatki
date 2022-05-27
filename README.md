# Приложение для подсчета очков на боулдеринг фестах

Django-based проект для создания и подсчета очков на соревнованиях по боулдерингу.

## Конфигурация
Изменяемые параметры в `src/app/.env`, для примера `src/app/.env.dev`

## Запуск на локальной машине
Требования python3.10 и pipenv.

Установка зависимостей:

```sh
cd src && pip install pipenv && pipenv install
cp app/.env.dev app/.env  # default environment variables
```

```sh
./manage.py migrate
./manage.py createsuperuser
```


Для разработки:

```sh
# run django dev server
$ ./manage.py runserver

```

### pylint

Добавить флаги в параметры pylint:

```
--load-plugins pylint_django --django-settings-module=app.settings
```

### Перевод

Cобрать все сообщения для перевода:

```sh
$ ./manage.py makemessages -l ru
$ ./manage.py compilemessages
```

## Docker

### Сборка образа

```sh
docker build -t nitrok/climbing .
```

### Запуск контейнера

```sh
docker run -v climbin_db:/var/lib/django-db -p "8000:8000" -it nitrok/climbing
```
