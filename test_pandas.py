import pandas as pd

data = [
    {"name": "Laptop", "price": 3000},
    {"name": "Phone", "price": 2000},
    {"name": "Mouse", "price": 100},
]

data2 = {'imie': ['Anna', 'Jan']}, {'wiek': [24, 25]}

df = pd.DataFrame(data)

print(df.describe(include='all'))