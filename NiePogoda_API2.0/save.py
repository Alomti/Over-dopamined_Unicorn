from pathlib import Path
import json
import logging
logger = logging.getLogger(__name__)
def save_result(name, names, extensions, label):
    if not name:
        logger.error('No folder has been chosen.')
        label.config(text='No folder has been chosen.')
        return
    path = Path(name)
    if path.suffix == '.txt':
        path.write_text(names + '' + extensions, encoding='utf-8')
        logger.info('Successfully saved')
        label.config(text='Successfully saved')
    elif path.suffix == '.json':
        with open (name, 'w', encoding='utf-8') as f:
            json.dump({'name': names, 'extension': extensions}, f, ensure_ascii=False, indent=4)
        logger.info('Successfully saved')
        label.config(text='Successfully saved')
    else:
        logger.error('Wrong file name or extension.')
        label.config(text='Wrong file name or extension.')