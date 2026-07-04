import sys
import logging
from pathlib import Path
import json
def setup_logging():
    try:
        base = Path(__file__).parent.parent
        default_log_file = Path(__file__).parent.parent / 'data' / 'app.log'
        using_default_log_file = False
        valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
        plik = Path(__file__).parent / 'config.json'
        
        if not plik.exists():
            raise FileNotFoundError('File "config.json" does not exists')
            
        with open(plik, 'r', encoding='utf-8') as f:
            config = json.load(f)
            if 'data_file' not in config:
                raise KeyError('No data_file in config.json')
            if 'log_level' not in config:
                raise KeyError('No log_level in config.json')
            if config['log_level'] not in valid_levels:
                raise ValueError('Wrong value in log_level in config.json')
            data_file = base / config['data_file']

            level = config['log_level']
            
            handlers = [logging.StreamHandler(sys.stdout)]

            if 'log_file' not in config:
                handlers.append(logging.FileHandler(default_log_file))
                using_default_log_file = True
            else:
                log_file = config['log_file']
                handlers.append(logging.FileHandler(base / log_file))

        logging.basicConfig(
            handlers=handlers,
            level=level,
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )
        logger = logging.getLogger(__name__)
        if using_default_log_file:
            logger.info('No log_file value in config.json. Default settings were used')
        logger.info('Logging setup succesfully configurated')
        return data_file
    except(FileNotFoundError ,KeyError, ValueError) as e:
        print(f'Error {e} in "config.json" file. Closing the program.')
        sys.exit()