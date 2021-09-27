class Product:
    def __init__(self, code, name, title, price):
        self.code = code
        self.name = name
        self.title = title
        self.price = price
        self.cnt = 1

    def add_cnt(self):
        self.cnt += 1

    def __repr__(self):
        return f'{{Code={self.code} Cnt={self.cnt} Price={self.price} Name="{self.name}"}}'


class ProductList:
    def __init__(self):
        self.pdict = {}

    def insert_product(self, code, name, title, price):
        if code in self.pdict:
            self.pdict[code].add_cnt()
        else:
            self.pdict[code] = Product(code, name, title, price)

    def get_products(self):
        return self.pdict.values()

    def __repr__(self):
        res = 'Products:{\n'
        for p in self.pdict.values():
            res += str(p) + '\n'
        res += ' }'
        return res
