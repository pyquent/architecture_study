from abc import ABC, abstractmethod

# Абстрактний клас ітератора
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Абстрактний клас агрегата
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Конкретний ітератор для списку
class ListIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = 0

    def has_next(self):
        return self._index < len(self._data)

    def next(self):
        if self.has_next():
            value = self._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration()

# Конкретний клас списку
class ListAggregate(Aggregate):
    def __init__(self):
        self._data = []

    def create_iterator(self):
        return ListIterator(self._data)

    def add_item(self, item):
        self._data.append(item)


if __name__ == "__main__":
    aggregate = ListAggregate()
    aggregate.add_item("Елемент 1")
    aggregate.add_item("Елемент 2")
    aggregate.add_item("Елемент 3")

    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())



"""
Патерн "Ітератор" визначає механізм обходу об'єкта без розкриття його внутрішньої структури. Він дозволяє послідовно отримувати доступ до елементів об'єкта.
"""
