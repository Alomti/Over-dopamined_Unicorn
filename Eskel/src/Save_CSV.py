from csv import writer, DictWriter
from pathlib import Path
from reports import Raports
from typing import TextIO
import pandas as pd

def report(file: TextIO, fieldnames: list, report: list):
    w = DictWriter(file, fieldnames)
    w.writeheader()
    for d in report:
        for key, value in d.items():
            w.writerow({'Liczba': key, 'Wynik': value})


def saveCSV():
    reports = Raports()
    
    report1 = Path(__file__).parent.parent / 'data' / 'report1.csv'
    report1.parent.mkdir(parents=True, exist_ok=True)
    with open(report1, 'w', newline='', encoding='utf-8') as f:
        w = writer(f)
        w.writerow(['Raport', '1'])
        fieldnames1 = ['Liczba', 'Wynik']
        report(f, fieldnames1, reports.raport1())

    report2 = Path(__file__).parent.parent / 'data' / 'report2.csv'
    report2.parent.mkdir(parents=True, exist_ok=True)
    with open(report2, 'w', encoding='utf-8') as f:
        pd.DataFrame(reports.raport2()).to_csv(f, index=False, encoding='utf-8')

    report3 = Path(__file__).parent.parent / 'data' / 'report3.csv'
    report3.parent.mkdir(parents=True, exist_ok=True)
    with open(report3, 'w', encoding='utf-8') as f:
        pd.DataFrame(reports.raport3()).to_csv(f, index=False, encoding='utf-8')

    report4 = Path(__file__).parent.parent / 'data' / 'report4.csv'
    report4.parent.mkdir(parents=True, exist_ok=True)
    with open(report4, 'w', encoding='utf-8') as f:
        pd.DataFrame(reports.raport4()).to_csv(f, index=False, encoding='utf-8')

    report5 = Path(__file__).parent.parent / 'data' / 'report5.csv'
    report5.parent.mkdir(parents=True, exist_ok=True)
    with open(report5, 'w', encoding='utf-8') as f:
        pd.DataFrame(reports.raport5()).to_csv(f, index=False, encoding='utf-8')

saveCSV()