import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(user)s'
)
logging.info('msg', extra={'user': 'hello there!'})
