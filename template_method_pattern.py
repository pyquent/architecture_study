from abc import ABC, abstractmethod

# Абстрактний клас з шаблонним методом
class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook()

    def base_operation1(self):
        print("Базова операція 1")

    def base_operation2(self):
        print("Базова операція 2")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def hook(self):
        pass

# Конкретний клас, який реалізує операції
class ConcreteClass(AbstractClass):
    def required_operation1(self):
        print("Реалізація операції 1 у конкретному класі")

    def hook(self):
        print("Додаткова операція (hook) у конкретному класі")

# Використання
if __name__ == "__main__":
    concrete_class = ConcreteClass()
    concrete_class.template_method()



"""
Патерн "Шаблонний метод" визначає загальну структуру алгоритму у базовому класі та дозволяє підкласам перевизначити певні кроки цього алгоритму без зміни його загальної структури.
"""
