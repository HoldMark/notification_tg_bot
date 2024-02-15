import json
import logging
from pydantic import BaseModel
from src.core.config import DATA_DIR

logger = logging.getLogger(f'bot.{__name__}')


class Text(BaseModel):
    list_of_text: list[str]
    greeting: str


try:

    logger.info('Try to get text data from file')

    with open(f'{DATA_DIR}/text_data.json', 'r', encoding='UTF-8') as file:
        json_text = json.load(file)

except Exception as e:

    logger.error(f'Failed to read file with data', exc_info=True)

TextData = Text(**json_text)
