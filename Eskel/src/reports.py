from api import Apiget
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
        Avg_cart = round(sum(carts) / len(carts), 2)
        return [{'Avg cart value:': Avg_cart}]
    
    def raport5(self):
        users = {}
        for c in self.api.getall_carts():
            users[c['userId']] = users.get(c['userId'], 0) + 1
        top3 = sorted(users.items(), key=lambda x: x[1], reverse=True)[:3]
        top3 = [{'userId': x, 'no_of_carts': y} for x, y in top3]
        return top3

if __name__ == '__main__':
    raports = Raports()
    print('1',raports.raport1())
    print('2',raports.raport2())
    print('3',raports.raport3())
    print('4',raports.raport4())
    print('5',raports.raport5())