from api import Apiget
import pandas as pd
from pathlib import Path
class Raports():
    def __init__(self):
        self.api = Apiget()

    def raport1(self):
        users = len(self.api.getall_users())
        carts = 0
        products = []
        for c in self.api.getall_carts():
            carts += 1
            for p in c['products']:
                products.append(p['quantity'])
        products = sum(products)
        return [{'Liczba produktów:': products}, {'Liczba koszyków:': carts}, {'Liczba użytkowników:': users}]
    
    def raport2(self):
        carts = pd.DataFrame(self.api.getall_carts())
        topproducts = carts.explode('products')
        top3 = pd.json_normalize(topproducts['products']).groupby('productId')['quantity'].sum().reset_index().sort_values('quantity', ascending=False).head(3)
        products = pd.DataFrame(self.api.getall_products())
        names = products[['id','title']]
        raport = pd.merge(top3, names, how='left', left_on='productId', right_on='id').drop(columns=['productId', 'id'])
        return raport
    
    def raport3(self):
        carts = []
        for c in self.api.getall_carts():
            c_price = 0
            c_products = c['products']
            for p in c_products:
                product = self.api.get_product(p['productId'])
                c_price += product['price']
            carts.append({'Cart_Id': c['id'], 'Cart_Price': c_price})
        carts = sorted(carts, key=lambda x: x['Cart_Price'], reverse=True)[:3]
        return carts
    
    def raport4(self):
        carts = []
        for c in self.api.getall_carts():
            c_price = 0
            c_products = c['products']
            for p in c_products:
                product = self.api.get_product(p['productId'])
                c_price += product['price']
            carts.append(c_price)
        Avg_cart = round(sum(carts) / len(carts), 2)
        return [{'Avg cart value:': Avg_cart}]
    
    def raport5(self):
        df = pd.DataFrame(self.api.getall_carts())
        top3 = df['userId'].value_counts().head(3).to_frame(name='count_of_carts').reset_index()
        return top3
    
    def raport6(self):
        c_df = pd.DataFrame(self.api.getall_carts()).explode('products')
        products_from_carts = pd.json_normalize(c_df['products']).groupby('productId')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
        p_df = pd.DataFrame(self.api.getall_products())
        categoty = p_df[['id','category']]
        result = pd.merge(products_from_carts, categoty, how='left', left_on='productId', right_on='id').drop(columns=['productId', 'id']).groupby('category')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
        return result

if __name__ == '__main__':
    raports = Raports()
    # print('1',raports.raport1())
    # print('2',raports.raport2())
    # print('3',raports.raport3())
    # print('4',raports.raport4())
    # print('5',raports.raport5())
    # print('6',raports.raport6())
    # print('7',raports.raport7())
    print(raports.raport6())
    report = Path(__file__).parent.parent / 'data' / 'current_report.csv'
    report.parent.mkdir(parents=True, exist_ok=True)
    raports.raport6().to_csv(report, index=False, encoding='utf-8')