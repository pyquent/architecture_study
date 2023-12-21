from abc import ABC, abstractmethod

# Абстрактний клас Стану
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Контекст, який управляє станами
class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Конкретний клас Стану A
class ConcreteStateA(State):
    def handle(self):
        print("Обробка стану A")
        # Зміна стану на інший
        # Контекст визначає, який саме стан буде встановлено

# Конкретний клас Стану B
class ConcreteStateB(State):
    def handle(self):
        print("Обробка стану B")
        # Зміна стану на інший
        # Контекст визначає, який саме стан буде встановлено


if __name__ == "__main__":
    # Початковий стан
    state_a = ConcreteStateA()
    context = Context(state_a)

    # Виклик методу обробки, який виконується у поточному стані
    context.request()

    # Зміна стану на інший
    state_b = ConcreteStateB()
    context.set_state(state_b)

    # Виклик методу обробки у новому стані
    context.request()




"""
Патерн "Стан" визначає сімейство класів, представляючих різні стани об'єкта, та об'єкт-контекст, який управляє переходами між цими станами.
"""
