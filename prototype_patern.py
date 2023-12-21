import copy

# Клас, який потрібно клонувати
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Конкретний клас, який реалізує клонування
class ConcretePrototype(Prototype):
    def __init__(self, data):
        self.data = data

    def show(self):
        print(f"Дані об'єкта: {self.data}")

if __name__ == "__main__":
    prototype = ConcretePrototype("початкові дані")

    cloned_object = prototype.clone()

    cloned_object.data = "нові дані"
    prototype.show()
    cloned_object.show()


"""
Патерн прототипу дозволяє створювати нові об'єкти, копіюючи старі, без залежності від їх конкретних класів.
"""
