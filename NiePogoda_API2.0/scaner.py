import logging
logger = logging.getLogger(__name__)
def get_data(folder):
    if not folder.is_dir():
        raise NotADirectoryError('Not a folder')
    data = {}
    for item in folder.iterdir():
        suffix = 'folder' if item.is_dir() else item.suffix or 'no extension'
        data[item.name] = suffix
    logger.info('Folder scanned succesfully')
    return data