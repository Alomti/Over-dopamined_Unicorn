from check_data import get_suffixes
import logging
logger = logging.getLogger(__name__)
class SRaport:
    def __init__(self, data):
        logger.info('Generating raport')
        self.suffixes = get_suffixes(data)

    def __str__(self):
        logger.info('Raport succesfully created')
        return f'{self.suffixes}'