import logging
logger = logging.getLogger(__name__)
try:
    from api import Apiget
except ModuleNotFoundError as e:
    logger.error(f'Error: Module not found {e}')
    SystemExit(1)
import pandas as pd
class Raports():
    try:
        def __init__(self):
            self.api = Apiget()
        
        def raport1(self):
            logger.info('Preparing raport 1')
            try:
                users = len(self.api.getall_users())
                carts = 0
                products = []
                for c in self.api.getall_carts():
                    carts += 1
                    for p in c['products']:
                        products.append(p['quantity'])
                products = sum(products)
                return [{'Liczba produktów:': products}, {'Liczba koszyków:': carts}, {'Liczba użytkowników:': users}]
            except Exception as e:
                logger.error(f'Error: {e} in raport 1')
            return []
        
        def raport2(self):
            logger.info('Preparing raport 2')
            try:
                carts = pd.DataFrame(self.api.getall_carts())
                topproducts = carts.explode('products')
                top3 = pd.json_normalize(topproducts['products']).groupby('productId')['quantity'].sum().reset_index().sort_values('quantity', ascending=False).head(3)
                products = pd.DataFrame(self.api.getall_products())
                names = products[['id','title']]
                raport = pd.merge(top3, names, how='left', left_on='productId', right_on='id').drop(columns=['productId', 'id'])
                return raport
            except Exception as e:
                logger.error(f'Error: {e} in raport 2')
            return pd.DataFrame()
        
        def raport3(self):
            logger.info('Preparing raport 3')
            try:
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
            except Exception as e:
                logger.error(f'Error: {e} in raport 3')
            return {None,None}
        
        def raport4(self):
            logger.info('Preparing raport 4')
            try:
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
            except Exception as e:
                logger.error(f'Error: {e} in raport 4')
            return []
        
        def raport5(self):
            logger.info('Preparing raport 5')
            try:
                df = pd.DataFrame(self.api.getall_carts())
                top3 = df['userId'].value_counts().head(3).to_frame(name='count_of_carts').reset_index()
                return top3
            except Exception as e:
                logger.error(f'Error: {e} in raport 5')
            return pd.DataFrame()
        
        def raport6(self):
            logger.info('Preparing raport 6')
            try:
                c_df = pd.DataFrame(self.api.getall_carts()).explode('products')
                products_from_carts = pd.json_normalize(c_df['products']).groupby('productId')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
                p_df = pd.DataFrame(self.api.getall_products())
                product_categories = p_df[['id','category']]
                result = pd.merge(products_from_carts, product_categories, how='left', left_on='productId', right_on='id').drop(columns=['productId', 'id']).groupby('category')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
                return result
            except Exception as e:
                logger.error(f'Error: {e} in raport 6')
            return pd.DataFrame()
        
        def raport7(self):
            logger.info('Preparing raport 7')
            try:
                c_df = pd.DataFrame(self.api.getall_carts()).explode('products')
                products = pd.json_normalize(c_df['products'])
                quantity_of_products = pd.DataFrame([{'Quantity of products in all carts': products['quantity'].sum()}])
                return quantity_of_products
            except Exception as e:
                logger.error(f'Error: {e} in raport 7')
            return pd.DataFrame()
    except Exception as e:
        logger.error(f'Unexpected error: {e}')

if __name__ == '__main__':
    raports = Raports()
    print('1',raports.raport1())
    print('2',raports.raport2())
    print('3',raports.raport3())
    print('4',raports.raport4())
    print('5',raports.raport5())
    print('6',raports.raport6())
    print('7',raports.raport7())