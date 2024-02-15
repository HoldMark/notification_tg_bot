import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
TG_USER_ID = os.environ.get("TG_USER_ID")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(CURRENT_DIR, '../../')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
DATA_DIR = os.path.join(BASE_DIR, 'data')
