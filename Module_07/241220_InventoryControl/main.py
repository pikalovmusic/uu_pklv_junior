class Product:
    def __init__(self, product_name: str, weight: float, category: str):
        self.name = product_name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            file = open(self.__file_name)  # 'r' тут можно не указывать
            products = file.read()
            file.close()
            return products
        except FileNotFoundError:
            return ''

    def add(self, *products: Product):
        slash_n = ''
        products_added = self.get_products()
        if products_added != '':
            slash_n = '\n'

        file = open(self.__file_name, 'a')

        for product in products:
            if products_added.__contains__(product.name):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{slash_n}{product}')
                slash_n = '\n'

        file.close()


# проверяем:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Doshirak', 0.2, 'Quickfood')

print(p2)  # __str__
s1.add(p1, p2, p3)
s1.add(p4)
print(s1.get_products())
