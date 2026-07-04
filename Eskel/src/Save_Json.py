try:
    from config.config_setup import setup_logging
    data_file = setup_logging()
except ModuleNotFoundError as e:
    print(f'Error: Module not found {e}')
    raise SystemExit(1)
import logging
logger = logging.getLogger(__name__)
import json
try:
    from pathlib import Path
except ModuleNotFoundError as e:
    logger.error(f'Unexcepted error: {e}')
    SystemExit(1)
try:
    from reports import Raports
except ModuleNotFoundError as e:
    logger.error(f'Unexcepted error: {e}')
    SystemExit(1)
try:
    import pandas as pd
except ModuleNotFoundError as e:
    logger.error(f'Unexcepted error: {e}')
    SystemExit(1)

try:
    def SaveJson():
        logger.info('Saving to JSON format...')
        reports = Raports()
        
        report1 = data_file / 'report1.json'
        report1.parent.mkdir(parents=True, exist_ok=True)
        with open(report1, 'w', encoding='utf-8') as f:
            json.dump(reports.raport1(), f, ensure_ascii=False, indent=4)
        
        report2 = data_file / 'report2.json'
        report2.parent.mkdir(parents=True, exist_ok=True)
        reports.raport2().to_json(report2, index=False, indent=4)
        
        report3 = data_file / 'report3.json'
        report3.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(reports.raport3()).to_json(report3, index=False, indent=4)
        
        report4 = data_file / 'report4.json'
        report4.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(reports.raport4()).to_json(report4, index=False, indent=4)
        
        report5 = data_file / 'report5.json'
        report5.parent.mkdir(parents=True, exist_ok=True)
        reports.raport5().to_json(report5, index=False, indent=4)
        
        report6 = data_file / 'report6.json'
        report6.parent.mkdir(parents=True, exist_ok=True)
        reports.raport6().to_json(report6, index=False, indent=4)
        
        report7 = data_file / 'report7.json'
        report7.parent.mkdir(parents=True, exist_ok=True)
        reports.raport7().to_json(report7, index=False, indent=4)
        logger.info('All JSON reports completed')
except PermissionError as e:
    logger.error(f'Error: Lack of permision to save in this file "{e}"')
except FileNotFoundError as e:
    logger.error(f'Error: Path does not exists "{e}"')
except Exception as e:
    logger.error(f'Unexpected error: {e}')
if __name__ == '__main__':
    SaveJson()