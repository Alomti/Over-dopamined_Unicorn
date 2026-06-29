import requests
import logging
logging.getLogger(__name__)

class Apiget():
    def __init__(self):
        self.base_url = 'https://fakestoreapi.com'

    def getall_products(self):
        products = requests.get(f'{self.base_url}/products')
        return products.json()
    
    def get_product(self, id):
        product = requests.get(f'{self.base_url}/products/{id}')
        return product.json()
    
    def getall_users(self):
        user = requests.get(f'{self.base_url}/users')
        return user.json()

    def get_user(self, id):
        user = requests.get(f'{self.base_url}/users/{id}')
        return user.json()
    
    def getall_carts(self):
        cart = requests.get(f'{self.base_url}/carts')
        return cart.json()

    def get_cart(self, id):
        cart = requests.get(f'{self.base_url}/carts/{id}')
        return cart.json()
    
if __name__ == '__main__':
    api = Apiget()
    print(api.getall_users())