from dataclasses import dataclass
import os


@dataclass
class TelegramBot:
    token: str
    admins: list[int]


def load_config():
    return TelegramBot(
        token=os.environ['BOT_TOKEN'],
        admins=list(map(int, os.environ['ADMINS'].split()))
    )
