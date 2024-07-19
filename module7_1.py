from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, "r")
        from pprint import pprint
        pprint(file.read())
        file.close()

    def add(self, *products):


        for i in range(len(products)):
            file = open(self.__file_name, "r")
            file_r = file.read()

            if products[i].name in file_r:
                print(f"Продукт {products[i].name} уже есть в магазине.")
            else:
                file1= open(self.__file_name, "a")
                product_added = f"{products[i]} '\n'"
                file1.write(product_added)


        file.close


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')



s1.add(p1, p2, p3)
