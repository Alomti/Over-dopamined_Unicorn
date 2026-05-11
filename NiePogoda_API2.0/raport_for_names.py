from check_data import get_names
import logging
logger = logging.getLogger(__name__)
class NRaport:
    def __init__(self, data):
        logger.info('Generating raport')
        self.names = get_names(data)

    def __str__(self):
        logger.info('Raport succesfully created')
        return f'{self.names}'