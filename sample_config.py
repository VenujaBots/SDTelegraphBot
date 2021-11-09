import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2121334565:AAGM5LvwIBk1nnWDYwu4aes0Sa7HaWAeIiY")

    APP_ID = int(os.environ.get("APP_ID", 7395896))

    API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")
