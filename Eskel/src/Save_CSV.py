from csv import writer, DictWriter
from pathlib import Path
from reports import Raports

def saveCSV():
    raports = Raports()
    path = Path(__file__).parent.parent / 'data' / 'raport.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        main_w = writer(f)

        main_w.writerow(['Raport', '1'])
        fieldnames = ['Liczba', 'Wynik']
        w = DictWriter(f, fieldnames)
        w.writeheader()
        raport1 = raports.raport1()
        for d in raport1:
            for key, value in d.items():
                w.writerow({'Liczba': key, 'Wynik': value})

        main_w.writerow(['Raport', '2'])
        fieldnames2 = ['productId', 'quantity']
        w2 = DictWriter(f, fieldnames2)
        w2.writeheader()
        raport2 = raports.raport2()
        w2.writerows(raport2)

        main_w.writerow(['Raport', '3'])
        fieldnames3 = ['Cart_Id', 'Cart_Price']
        w3 = DictWriter(f, fieldnames3)
        w3.writeheader()
        raport3 = raports.raport3()
        w3.writerows(raport3)

        fieldnames4 = ['Raport', '4']
        w4 = DictWriter(f, fieldnames4)
        w4.writeheader()
        raport4 = raports.raport4()
        for key, value in raport4.items():
            w4.writerow({'Liczba': key, 'Wynik': value})

        main_w.writerow(['Raport', '5'])
        fieldnames5 = ['userId', 'no_of_carts']
        w5 = DictWriter(f, fieldnames5)
        w5.writeheader()
        raport5 = raports.raport5()
        w5.writerows(raport5)

saveCSV()