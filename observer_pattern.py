from abc import ABC, abstractmethod
from typing import List

# Абстрактний клас Спостеріганого
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Абстрактний клас Спостерігача
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Конкретний клас Спостеріганого
class ConcreteSubject(Subject):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def some_business_logic(self):
        # Зміни в стані спостеріганого об'єкта, які спричиняють виклик notify()
        self.notify()

# Конкретний клас Спостерігача
class ConcreteObserver(Observer):
    def update(self):
        print("Спостерігач отримав оновлення")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer1)

    subject.some_business_logic()



"""
Патерн "Спостерігач" визначає залежність між об'єктом, який називається "Спостеріганим", та об'єктами, які його спостерігають (спостерігачами).
Коли спостерігане об'єкт змінює свій стан, всі його спостерігачі отримують повідомлення та автоматично оновлюють свій стан.
"""
