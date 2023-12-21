from abc import ABC, abstractmethod

# Абстрактний клас для продукту A
class AbstractProductA(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Абстрактний клас для продукту B
class AbstractProductB(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретний продукт A1
class ConcreteProductA1(AbstractProductA):
    def operation(self) -> str:
        return "Виклик операції у продукті A1"

# Конкретний продукт B1
class ConcreteProductB1(AbstractProductB):
    def operation(self) -> str:
        return "Виклик операції у продукті B1"

# Абстрактний клас для фабрики
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Конкретна фабрика 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# Використання
if __name__ == "__main__":
    factory = ConcreteFactory1()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.operation())
    print(product_b.operation())


"""
Абстрактна фабрика визначає інтерфейс для створення сімейства пов'язаних або взаємозалежних об'єктів без конкретної специфікації їх класів.
"""
