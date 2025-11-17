from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from telegram.ext import Application
from bot.handlers import register_handlers

class Command(BaseCommand):
    help = "Run the Telegram bot via long-polling"

    def handle(self, *args, **options):
        token = settings.TELEGRAM_BOT_TOKEN
        if not token:
            raise CommandError("TELEGRAM_BOT_TOKEN missing. Put it in .env")
        app = Application.builder().token(token).build()
        register_handlers(app)
        self.stdout.write(self.style.SUCCESS("Starting Telegram bot (polling)…"))
        app.run_polling(allowed_updates=None)
