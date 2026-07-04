import logging
logger = logging.getLogger(__name__)
try:
    import requests
except ModuleNotFoundError as e:
    logger.error(f'Unexcepted error: {e}')
    SystemExit(1)

class Apiget():
    def __init__(self):
        self.base_url = 'https://fakestoreapi.com'
        self.timeout = 10
    
    def save_get(self, url):
        try:
            responce = requests.get(url, timeout=self.timeout)
            responce.raise_for_status()
            return responce.json()
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Server connection error for URL {url}: {e}")
            SystemExit(1)
        except requests.exceptions.Timeout as e:
            logger.error(f"Responce timeout for URL {url}: {e}")
            SystemExit(1)
        except requests.exceptions.HTTPError as e:
            logger.error(f"Server returned an HTTP error for URL {url}: {e}")
            SystemExit(1)
        except requests.exceptions.JSONDecodeError as e:
            logger.error(f"The responce from URL {url} is not a valid JSON format: {e}")
            SystemExit(1)
        except requests.exceptions.RequestException as e:
            logger.error(f"Unexcepted error requests for URL {url}: {e}")
            SystemExit(1)

    def getall_products(self):
        return self.save_get(f'{self.base_url}/products')
    
    def get_product(self, id):
        return self.save_get(f'{self.base_url}/products/{id}')
    
    def getall_users(self):
        return self.save_get(f'{self.base_url}/users')

    def get_user(self, id):
        return self.save_get(f'{self.base_url}/users/{id}')
    
    def getall_carts(self):
        return self.save_get(f'{self.base_url}/carts')

    def get_cart(self, id):
        return self.save_get(f'{self.base_url}/carts/{id}')
    
if __name__ == '__main__':
    api = Apiget()
    print(api.getall_users())