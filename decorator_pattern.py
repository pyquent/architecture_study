from abc import ABC, abstractmethod

# Компонент, який визначає спільний інтерфейс для всіх конкретних компонентів
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Конкретний компонент
class ConcreteComponent(Component):
    def operation(self):
        return "Оригінальна операція конкретного компонента"

# Базовий декоратор
class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

# Конкретний декоратор, який додає додатковий функціонал
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"Додатковий функціонал від ConcreteDecoratorA\n{super().operation()}"

# Ще один конкретний декоратор, який також додає свій функціонал
class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"Додатковий функціонал від ConcreteDecoratorB\n{super().operation()}"

# Використання
if __name__ == "__main__":
    # Спочатку маємо оригінальний компонент
    component = ConcreteComponent()
    print("1. Оригінальний компонент:")
    print(component.operation())

    # Потім обгортаємо його декоратором A
    decorator_a = ConcreteDecoratorA(component)
    print("\n2. Декоратор A:")
    print(decorator_a.operation())

    # Додаємо ще один декоратор B
    decorator_b = ConcreteDecoratorB(decorator_a)
    print("\n3. Декоратор B:")
    print(decorator_b.operation())


"""
Патерн "Декоратор" використовується для динамічного додавання нових обов'язків об'єктам за допомогою обгорток.
"""
