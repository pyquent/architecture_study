from abc import ABC, abstractmethod

# Абстракція
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return f"Абстракція: {self.implementation.operation_implementation()}"

# Реалізація
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

# Конкретна реалізація A
class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "Виклик операції у конкретній реалізації A"

# Конкретна реалізація B
class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "Виклик операції у конкретній реалізації B"

if __name__ == "__main__":
    implementation_a = ConcreteImplementationA()
    abstraction_a = Abstraction(implementation_a)
    print(abstraction_a.operation())

    implementation_b = ConcreteImplementationB()
    abstraction_b = Abstraction(implementation_b)
    print(abstraction_b.operation())


"""
Патерн "Міст" використовується для відокремлення абстракції від реалізації так, щоб обидві можливо було змінювати незалежно одна від одної.
"""
