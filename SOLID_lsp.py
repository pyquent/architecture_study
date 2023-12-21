# Неправильно з дотриманням LSP
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    # Острич не вміє літати
    def fly(self):
        raise NotImplementedError("Острич не може літати")

# Помилка при використанні LSP
def make_bird_fly(bird):
    bird.fly()



# Правильне
class Bird:
    def move(self):
        pass

class Ostrich(Bird):
    # Острич реалізує метод руху, але не літає
    def move(self):
        print("Острич бігає")

# Використання LSP
def make_bird_move(bird):
    bird.move()
