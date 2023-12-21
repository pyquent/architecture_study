import copy

# Оригінальний клас, стан якого ми хочемо зберегти
class Originator:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self._state = memento.get_state()

# Знімок стану об'єкта
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Опікун, що відповідає за зберігання та відновлення знімків стану
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Використання
if __name__ == "__main__":
    originator = Originator("Початковий стан")

    # Збереження стану
    memento1 = originator.create_memento()

    # Зміна стану
    originator.set_state("Новий стан")

    # Збереження стану зміненого об'єкта
    memento2 = originator.create_memento()

    # Відновлення початкового стану
    originator.restore_memento(memento1)
    print(f"Поточний стан після відновлення: {originator.get_state()}")

    # Відновлення зміненого стану
    originator.restore_memento(memento2)
    print(f"Поточний стан після відновлення: {originator.get_state()}")



"""
Патерн "Знімок" визначає, як зберегти та відновити попередні стани об'єктів без розкриття їхньої внутрішньої реалізації.
"""
