class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(f"ID першого екземпляра: {id(singleton1)}")
    print(f"ID другого екземпляра: {id(singleton2)}")


"""
Патерн одинака гарантує існування лише одного екземпляра класу та забезпечує глобальний доступ до нього.
"""
