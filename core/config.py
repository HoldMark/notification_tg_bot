import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
TG_USER_ID = os.environ.get("TG_USER_ID")

TEXTS = [
    'Выпрями спину!',
    'Молодец, что держишь спину ровной!',
    'Выравни  спину!',
    'Осанка!',
    'Держи спину ровно!',
    'Расправь плечи!',
    'Прямая спина!'
]
