from abc import ABC, abstractmethod

# Абстрактний клас стратегії
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Контекст, який використовує стратегію
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# Конкретна стратегія A
class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Виконання стратегії A")

# Конкретна стратегія B
class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Виконання стратегії B")

# Використання
if __name__ == "__main__":
    # Початкова стратегія
    strategy_a = ConcreteStrategyA()
    context = Context(strategy_a)

    # Виклик методу стратегії A
    context.execute_strategy()

    # Зміна стратегії на B
    strategy_b = ConcreteStrategyB()
    context.set_strategy(strategy_b)

    # Виклик методу стратегії B
    context.execute_strategy()



"""
Патерн "Стратегія" визначає родину алгоритмів, упакованих в окремі класи, і робить їх взаємозамінними.
Клас, який використовує алгоритм, може легко змінювати його, не змінюючи свій власний код.
"""
