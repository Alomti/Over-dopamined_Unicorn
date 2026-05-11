import sys
import logging
from pathlib import Path
import json
def setup_logging():
    try:
        using_default_log_file = False
        valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
        plik = Path(__file__).parent / 'config.json'
        
        if not plik.exists():
            raise FileNotFoundError('File "config.json" do not exists')
            
        with open(plik, 'r', encoding='utf-8') as f:
            config = json.load(f)
            if 'log_level' not in config:
                raise KeyError('No log_level in config.json')
            if config['log_level'] not in valid_levels:
                raise ValueError('Wrong value in log_level in config.json')
            level = config['log_level']
            
            handlers = [logging.StreamHandler(sys.stdout)]

            if 'log_file' not in config:
                handlers.append(logging.FileHandler('app.log'))
                using_default_log_file = True
            else:
                handlers.append(logging.FileHandler(config['log_file']))

        logging.basicConfig(
            handlers=handlers,
            level=level,
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )
        logger = logging.getLogger(__name__)
        if using_default_log_file:
            logger.info('No log_file value in config.json. Default settings were used')
        logger.info('Logging setup succesfully configurated')
    except(FileNotFoundError ,KeyError, ValueError) as e:
        print(f'Error {e} in "config.json" file. Closing the program.')
        sys.exit()