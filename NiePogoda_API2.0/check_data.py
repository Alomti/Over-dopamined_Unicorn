import logging
logger = logging.getLogger(__name__)
def get_names(data):
    keys = list(data.keys())
    logger.info('file names succesfully downloaded')
    return keys
    
def get_suffixes(data):
    no_of_suf = {}
    array = list(data.values())
    for i in array:
        no_of_suf[i] = no_of_suf.get(i, 0) + 1
    logger.info('file extensions succesfully downloaded')
    return no_of_suf