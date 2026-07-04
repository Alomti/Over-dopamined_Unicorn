try:
    from config.config_setup import setup_logging
    data_file = setup_logging()
except ModuleNotFoundError as e:
    print(f'Error: Module not found {e}')
    raise SystemExit(1)
import logging
logger = logging.getLogger(__name__)
try:
    from csv import writer, DictWriter
except ModuleNotFoundError as e:
    logger.error(f'Error: Module not found {e}')
    SystemExit(1)
try:
    from reports import Raports
except ModuleNotFoundError as e:
        logger.error(f'Error: Module not found {e}')
        raise SystemExit(1)
try:
    from typing import TextIO
except ModuleNotFoundError as e:
        logger.error(f'Error: Module not found {e}')
        raise SystemExit(1)
try:
    import pandas as pd
except ModuleNotFoundError as e:
        logger.error(f'Error: Module not found {e}')
        raise SystemExit(1)

def report(file: TextIO, fieldnames: list, report: list):
    w = DictWriter(file, fieldnames)
    w.writeheader()
    for d in report:
        for key, value in d.items():
            w.writerow({'Liczba': key, 'Wynik': value})
try:
    def saveCSV():
        logger.info('Saving to CSV format...')
        reports = Raports()
        
        report1 = data_file / 'report1.csv'
        report1.parent.mkdir(parents=True, exist_ok=True)
        with open(report1, 'w', newline='', encoding='utf-8') as f:
            w = writer(f)
            w.writerow(['Raport', '1'])
            fieldnames1 = ['Liczba', 'Wynik']
            report(f, fieldnames1, reports.raport1())

        report2 = data_file / 'report2.csv'
        report2.parent.mkdir(parents=True, exist_ok=True)
        reports.raport2().to_csv(report2, index=False, encoding='utf-8')

        report3 = data_file / 'report3.csv'
        report3.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(reports.raport3()).to_csv(report3, index=False, encoding='utf-8')

        report4 = data_file / 'report4.csv'
        report4.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(reports.raport4()).to_csv(report4, index=False, encoding='utf-8')

        report5 = data_file / 'report5.csv'
        report5.parent.mkdir(parents=True, exist_ok=True)
        reports.raport5().to_csv(report5, index=False, encoding='utf-8')

        report6 = data_file / 'report6.csv'
        report6.parent.mkdir(parents=True, exist_ok=True)
        reports.raport6().to_csv(report6, index=False, encoding='utf-8')

        report7 = data_file / 'report7.csv'
        report7.parent.mkdir(parents=True, exist_ok=True)
        reports.raport7().to_csv(report7, index=False, encoding='utf-8')
        logger.info('All CSV reports completed')
except PermissionError as e:
    logger.error(f'Error: Lack of permision to save in this file "{e}"')
except FileNotFoundError as e:
    logger.error(f'Error: Path does not exists "{e}"')
except Exception as e:
    logger.error(f'Unexpected error: {e}')

if __name__ == '__main__':
     saveCSV()