import logging
logger = logging.getLogger(__name__)
from pathlib import Path
from raport_for_names import NRaport
from raport_for_suffixes import SRaport
from scaner import get_data
def callback(choice, info_label):
    try:
        if not choice:
            logger.error('No folder has been chosen.')
            info_label.config(text='No folder has been chosen.')
            return False, False
        input_folder = choice
        logger.info(f'Selected {input_folder}')
        if not input_folder:
            raise ValueError('Name cannot be empty')
        
        folder = Path(input_folder)
        if not folder.exists():
            raise FileNotFoundError(f'Folder {folder} does not exists')
        if not folder.is_dir():
            raise NotADirectoryError(f'{folder} is not a folder')
        data = get_data(folder)
        names = NRaport(data)
        suffixes = SRaport(data)
        logger.info('Program worked correctly')
        return names, suffixes
    except (ValueError, FileNotFoundError, NotADirectoryError) as e:
        logger.error(f'Error {e}')
    except Exception as e:
        logger.error(f'Unexpected Error {e}')