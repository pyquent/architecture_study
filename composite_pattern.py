from abc import ABC, abstractmethod

# Компонент, який визначає спільний інтерфейс для всіх конкретних компонентів та їх складових
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Листок, який представляє індивідуальний об'єкт
class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Листок {self.name}"

# Композит, який може містити інші компоненти (композити та листки)
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [f"Група {self.name}:"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)


if __name__ == "__main__":
    leaf1 = Leaf("Листок 1")
    leaf2 = Leaf("Листок 2")

    composite = Composite("Складний об'єкт")
    composite.add(leaf1)
    composite.add(leaf2)

    client_code(composite, leaf1, leaf2)

def client_code(component1, component2, component3):
    print("Результат клієнтського коду:")
    print(component1.operation())
    print(component2.operation())
    print(component3.operation())



"""
Патерн "Компонувальник" дозволяє клієнтам обробляти як окремі об'єкти, так і їхні складові уніфікованим способом.
"""
