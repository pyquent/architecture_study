# Клас, який представляє продукт
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        print("Вигляд продукту:")
        for part in self.parts:
            print(part)

# Абстрактний будівельник
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass

# Конкретний будівельник
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):

"""
Патерн будівельника використовується для конструювання складних об'єктів крок за кроком.
Клас Director визначає порядок будівництва, а клас Builder відповідає за створення самого об'єкта.
"""
