from api import Apiget
class Raports():
    def __init__(self):
        self.api = Apiget()

    def raport1(self):
        users = 0
        for u in self.api.getall_users():
            users += 1
        carts = 0
        products = []
        for c in self.api.getall_carts():
            carts += 1
            for p in c['products']:
                products.append(p['quantity'])
        products = sum(products)
        return products, carts, users
    
    def raport2(self):
        products = []
        for c in self.api.getall_carts():
            for p in c['products']:
                products.append(p)
        products = sorted(products, key=lambda x: x['quantity'], reverse=True)[:3]

        for p in products:
            p_n = self.api.get_product(p['productId'])
            p['productId'] = p_n['title']
        return products
    
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
        Avg_cart = sum(carts) / len(carts)
        print(Avg_cart)


raport = Raports()
raport.raport4()