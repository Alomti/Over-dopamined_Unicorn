from pathlib import Path
import json
from reports import Raports
import pandas as pd

def SaveJson():
    reports = Raports()

    report1 = Path(__file__).resolve().parent.parent / 'data' / 'report1.json'
    report1.parent.mkdir(parents=True, exist_ok=True)
    with open(report1, 'w', encoding='utf-8') as f:
        json.dump(reports.raport1(), f, ensure_ascii=False, indent=4)

    report2 = Path(__file__).resolve().parent.parent / 'data' / 'report2.json'
    report2.parent.mkdir(parents=True, exist_ok=True)
    reports.raport2().to_json(report2, index=False, indent=4)

    report3 = Path(__file__).resolve().parent.parent / 'data' / 'report3.json'
    report3.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(reports.raport3()).to_json(report2, index=False, indent=4)

    report4 = Path(__file__).resolve().parent.parent / 'data' / 'report4.json'
    report4.parent.mkdir(parents=True, exist_ok=True)
    with open(report4, 'w', encoding='utf-8') as f:
        json.dump(reports.raport4(), f, ensure_ascii=False, indent=4)

    report5 = Path(__file__).resolve().parent.parent / 'data' / 'report5.json'
    report5.parent.mkdir(parents=True, exist_ok=True)
    reports.raport5().to_json(report5, index=False, indent=4)

    report6 = Path(__file__).resolve().parent.parent / 'data' / 'report6.json'
    report6.parent.mkdir(parents=True, exist_ok=True)
    reports.raport6().to_json(report6, index=False, indent=4)

    report7 = Path(__file__).resolve().parent.parent / 'data' / 'report7.json'
    report7.parent.mkdir(parents=True, exist_ok=True)
    reports.raport7().to_json(report7, index=False, indent=4)

if __name__ == '__main__':
    SaveJson()