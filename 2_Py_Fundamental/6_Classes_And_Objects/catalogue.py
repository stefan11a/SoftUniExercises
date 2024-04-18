class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [index for index in self.products if index[0] == first_letter]

    def __repr__(self):
        final_product_list = '\n'.join((sorted(self.products)))
        return f"Items in the {self.name} catalogue:\n{final_product_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product('1')
catalogue.add_product('2')
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
