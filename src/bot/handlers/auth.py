import json

from telegram import Update
from telegram.ext import CallbackContext

from devyatki.models import User


def command_start(update: Update, context: CallbackContext) -> None:
    if not update.message or not update.message.text:
        return None

    telegram_user_name = update.message.from_user.username;
    user, created = User.objects.get_or_create(telegram_username=telegram_user_name, username=telegram_user_name)

    if created:
        user.telegram_chat_id = update.effective_user.id
        user.telegram_data = json.dumps({
            "id": update.effective_user.id,
            "username": update.effective_user.username,
            "first_name": update.effective_user.first_name,
            "last_name": update.effective_user.last_name,
            "language_code": update.effective_user.language_code,
        })
        user.save()

        update.effective_chat.send_message(f"Приятно познакомиться, @{telegram_user_name}")
        update.message.delete()

    if not user.is_approved:
        update.effective_chat.send_message(f"Теперь осталось пройти модерацию. Пришли фото машины с номером 999.")

    # Refresh the cache by deleting and requesting it again
    # flush_users_cache()
    # cached_telegram_users()

    return None
