# Бот для фотографий машин с 999 в номере

Django-based телеграм бот собирающий фотографии машин с 999 в номере. Если фотография проходит модерацию - она попадает в закрытую группу.

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
$ python bot/main.py

```

### pylint

Добавить флаги в параметры pylint:

```
--load-plugins pylint_django --django-settings-module=app.settings
```



## Docker

### Сборка образа

```sh
docker build -t nitrok/devyatki .
```

### Запуск контейнера

```sh
docker run -v devyatki_db:/var/lib/django-db -p "8000:8000" -it nitrok/devyatki
```
