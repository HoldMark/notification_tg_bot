import random
from src.utils.get_text_data import TextData


def get_random_text(list_str: list[str] = TextData.list_of_text):
    return random.choice(list_str)
