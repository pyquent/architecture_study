from abc import ABC, abstractmethod

# Абстрактний клас для продукту
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретний продукт
class ConcreteProduct(Product):
    def operation(self) -> str:
        return "Виклик операції у конкретному продукті"

# Абстрактний клас для фабричного методу
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Результат виклику фабричного методу: {product.operation()}"
        return result

# Конкретний творець
class ConcreteCreator(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct()

# Використання
if __name__ == "__main__":
    creator = ConcreteCreator()
    result = creator.some_operation()
    print(result)

"""
Фабричний метод визначає інтерфейс для створення об'єкта, але залишає підкласам вирішення, який саме клас створювати.
Цей патерн дозволяє класу делегувати процес створення екземпляра своїм підкласам.
"""
