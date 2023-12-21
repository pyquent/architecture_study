class Adaptee:
    def specific_request(self):
        return "Виклик конкретного запиту"

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Адаптер: {self.adaptee.specific_request()}"

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    # Виклик методу через адаптер
    result = adapter.request()
    print(result)


"""
Патерн адаптера використовується для забезпечення взаємодії між класами, які мають несумісні інтерфейси.
"""
