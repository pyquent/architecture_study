# Використання розділених інтерфейсів
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

# Класи робітників тепер використовують лише ті інтерфейси, які є необхідними для них
class Worker(Workable, Eatable):
    pass

class Robot(Workable):
    pass
