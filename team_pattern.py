from abc import ABC, abstractmethod

# Абстрактний клас команди
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретна команда
class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.action()

# Виконавець (отримувач), який виконує конкретні дії
class Receiver:
    def action(self):
        return "Виконано виконавцем"

# Об'єкт, що викликає команди
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        return self.command.execute()

if __name__ == "__main__":
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)

    invoker = Invoker()
    invoker.set_command(concrete_command)

    result = invoker.execute_command()
    print(result)



"""
Патерн "Команда" використовується для інкапсуляції запитів як об'єкти, дозволяючи параметризувати клієнта запитами, чергувати їх, а також підтримувати скасування операцій.
"""
