from dataclasses import dataclass
import os
from environs import Env


@dataclass
class TelegramBot:
    token: str
    admins: list[int]


def load_config(path: str=None):
    env = Env()
    env.read_env(path)
    print(env.str("BOT_TOKEN"))
    print(env.list('ADMINS'))
    return TelegramBot(
        token=env.str("BOT_TOKEN"),
        admins=list(map(int, env.list("ADMINS")))
    )
