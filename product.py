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
    def __init__(self, perform_filter=False, filter_text=''):
        self.pdict = {}
        self.perform_filter = perform_filter
        self.filter_text = filter_text

    def insert_product(self, code, name, title, price, filter_value=''):
        if self.perform_filter and self.filter_text not in filter_value:
            return

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
