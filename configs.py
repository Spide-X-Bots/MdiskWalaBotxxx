# (c) @RoyalKrrishna

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    BACKUP_CHANNEL = os.environ.get("BACKUP_CHANNEL")
    GROUP_USERNAME = os.environ.get("GROUP_USERNAME")
    START_MSG = os.environ.get("START_MSG")
    START_PHOTO = os.environ.get("START_PHOTO")
    HOME_TEXT = os.environ.get("HOME_TEXT")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.environ.get("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.environ.get("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 300))
    MDISK_API = os.environ.get("MDISK_API", "12334")
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Robot.

🤖 My Name: <a href='https://t.me/MdiskSearchRobot'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.telethon.org'>Telethon</a>

📡 Server: <a href='https://heroku.com'>Heroku</a></b>
"""

    ABOUT_HELP_TEXT = """
<b>
👨‍💻 Developer : <a href='https://t.me/RoyalKrrishna'>Owener</a></b>
"""
