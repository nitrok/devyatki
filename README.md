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
mkdir devyatki_data
docker run -v $(pwd)/devyatki_data:/var/lib/mysql \ 
      -p "8816:8816" \
      -e TELEGRAM_TOKEN=token \ 
      -e SECRET_KEY=secret \
      -it nitrok/devyatki make docker-run-bot
```
или
```sh
cp ./src/.env.dev .env
docker-compose up
```
