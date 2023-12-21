from abc import ABC, abstractmethod

# Абстрактний клас реального об'єкта та його замісника
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Реальний об'єкт, до якого буде звертатися клієнт
class RealSubject(Subject):
    def request(self):
        return "Виклик операції у реальному об'єкті"

# Замісник, який контролює доступ до реального об'єкта
class Proxy(Subject):
    def __init__(self):
        self.real_subject = None

    def request(self):
        # Ліниве завантаження реального об'єкта
        if not self.real_subject:
            self.real_subject = RealSubject()
        return f"Виклик операції у заміснику, який викликає реальний об'єкт\n{self.real_subject.request()}"

if __name__ == "__main__":
    proxy = Proxy()
    result = proxy.request()
    print(result)



"""
Патерн "Замісник" надає об'єкт-замісник, який діє як проміжний шар між клієнтом та реальним об'єктом.
Він може використовуватися для лінивого завантаження, контролю доступу, кешування тощо.
"""
