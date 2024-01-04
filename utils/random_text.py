import random
from core.config import TEXTS


def get_random_text():
    return random.choice(TEXTS)
