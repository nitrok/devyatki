import logging
import os
import sys

import django

# IMPORTANT: this should go before any django-related imports (models, apps, settings)
# These lines must be kept together till THE END
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
# THE END

from django.conf import settings
from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, \
    CallbackQueryHandler
from bot.handlers import auth, moderation


log = logging.getLogger(__name__)


def command_help(update: Update, context: CallbackContext) -> None:
    update.effective_chat.send_message(
        "𝟗❾⑼️ <b>Я — бот для трех девяток</b>\n\n"
        "Через меня можно отправить картинку с автомобильным номером с 999 и заработать немного кармы\n\n "
        # "/top - Топ событий в Клубе\n\n"
        # "/random - Почитать случайный пост (неплохо убивает время)\n\n"
        # "/whois - Узнать профиль по телеграму\n\n"
        # "/horo - Клубный гороскоп\n\n"
        # "/invite - Попросить ссылку на доступ в группу\n\n"
        "/help - Справка",
        parse_mode=ParseMode.HTML
    )



def private_photo(update: Update, context: CallbackContext) -> None:
    # users = cached_telegram_users()
    # print('PRIVATE ')
    # print(update)

    if update.message.photo:
        context.bot_data[update.message.message_id] = update.message
        context.bot.forward_message(chat_id=settings.TELEGRAM_ADMIN_CHAT_ID,
                                    from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)

        keyboard = [
            [
                InlineKeyboardButton("Йеп 👍", callback_data=f"approve_photo:{update.message.message_id}"),
                InlineKeyboardButton("Ноуп 👎", callback_data=f"reject_photo:{update.message.message_id}"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=settings.TELEGRAM_ADMIN_CHAT_ID, text='О, великий, твоя воля?',
                                 reply_markup=reply_markup)



def main() -> None:
    # Initialize telegram
    updater = Updater(settings.TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Admin callbacks
    dispatcher.add_handler(CallbackQueryHandler(moderation.approve_photo, pattern=r"^approve_photo:.+"))
    dispatcher.add_handler(CallbackQueryHandler(moderation.reject_photo, pattern=r"^reject_photo:.+"))

    # Public + private chats
    dispatcher.add_handler(CommandHandler("help", command_help))
    # dispatcher.add_handler(CommandHandler("top", top.command_top))

    # Only private chats
    dispatcher.add_handler(CommandHandler("start", auth.command_start, Filters.chat_type.private))
    dispatcher.add_handler(MessageHandler(Filters.chat_type.private & Filters.photo, private_photo))

    # Start the bot
    if settings.DEBUG:
        updater.start_polling()
        # ^ polling is useful for development since you don't need to expose webhook endpoints
    else:
        updater.start_webhook(
            listen=settings.TELEGRAM_BOT_WEBHOOK_HOST,
            port=settings.TELEGRAM_BOT_WEBHOOK_PORT,
            url_path=settings.TELEGRAM_TOKEN,
        )
        log.info(f"Set webhook: {settings.TELEGRAM_BOT_WEBHOOK_URL + settings.TELEGRAM_TOKEN}")
        updater.bot.set_webhook(settings.TELEGRAM_BOT_WEBHOOK_URL + settings.TELEGRAM_TOKEN)

    # Wait all threads
    updater.idle()


if __name__ == '__main__':
    main()
