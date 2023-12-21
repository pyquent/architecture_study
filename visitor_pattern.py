from abc import ABC, abstractmethod

# Абстрактний клас елементу
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Конкретний клас елементу A
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

# Конкретний клас елементу B
class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

# Абстрактний клас відвідувача
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass

# Конкретний клас відвідувача
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print(f"Відвідувач обробляє елемент A: {element}")

    def visit_element_b(self, element):
        print(f"Відвідувач обробляє елемент B: {element}")

# Використання
if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor = ConcreteVisitor()

    for element in elements:
        element.accept(visitor)



"""
Патерн "Відвідувач" дозволяє визначити нові операції, не змінюючи класи елементів, поєднуючи їх у об'єкт-відвідувач.
Він визначає інтерфейс відвідувача з методами для кожного класу елемента.
"""
