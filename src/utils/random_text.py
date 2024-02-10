import random
from src.data.text import STRAIGHT_BACK_TEXT_LIST


def get_random_text(list_str: list[str] = STRAIGHT_BACK_TEXT_LIST):
    return random.choice(list_str)
