import pandas as pd

data = [
    {"name": "Laptop", "price": 3000},
    {"name": "Phone", "price": 2000},
    {"name": "Mouse", "price": 100},
]

data2 = {'imie': ['Anna', 'Jan']}, {'wiek': [24, 25]}

data3 = [{'name': 'Angelika'}]


data4 = {'Imię': ['Anna', 'Jan'], 'Wiek': [32, 60]}

df = pd.DataFrame(data4)

for index, row in df.iterrows():
    print(f"Indeks: {index}")
    print(f"Imię: {row['Imię']}, Wiek: {row['Wiek']}")
    for i, value in enumerate(row, start=1):
        print(i, value)
    print("-" * 20)




print(df)