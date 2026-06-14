import pandas as pd

data = [
    {"name": "Laptop", "price": 3000},
    {"name": "Phone", "price": 2000},
    {"name": "Mouse", "price": 100},
]

df = pd.DataFrame(data)

for x in df:
    print(x)