class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    def create(self):
        print(f'Pizza({self.name}) created with ingredients: {self.ingredients!r}')
    
    @staticmethod
    def get_sizes():
        return ['A', 'B', 'C']

    @classmethod
    def margherita(cls):
        return cls('margherita', ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls('prosciutto', ['mozzarella', 'tomatoes', 'ham'])

margherita = Pizza.margherita()
prosciutto = Pizza.prosciutto()

print('margherita:', margherita)
print('prosciutto:', prosciutto)
print('Pizza Sizes:', Pizza.get_sizes())

margherita.create()
prosciutto.create()