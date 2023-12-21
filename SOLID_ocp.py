# Неправильно з дотриманням OCP
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Функція, яка обчислює площу прямокутника
def calculate_area(rectangle):
    return rectangle.width * rectangle.height

# При додаванні нової фігури (круга) код функції змінюється
class Circle:
    def __init__(self, radius):
        self.radius = radius

# Змінений код для обчислення площі круга
def calculate_area(shape):
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Circle):
        return 3.14 * shape.radius * shape.radius
