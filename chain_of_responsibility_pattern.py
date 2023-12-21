from abc import ABC, abstractmethod

# Абстрактний клас обробника
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# Конкретний обробник A
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return "Оброблено обробником A"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return "Не вдалося обробити запит"

# Конкретний обробник B
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return "Оброблено обробником B"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return "Не вдалося обробити запит"


if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    handler_a.successor = handler_b

    # Виклик ланцюжка обов'язків
    result_a = handler_a.handle_request("A")
    print(result_a)

    result_b = handler_a.handle_request("B")
    print(result_b)

    result_c = handler_a.handle_request("C")
    print(result_c)



"""
Патерн "Ланцюжок обов'язків" використовується для передачі запитів послідовно через ланцюжок обробників.
Кожен обробник визначає, чи він може обробити запит, і передає його наступному обробнику в ланцюжку.
"""
