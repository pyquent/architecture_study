# Підсистема для взаємодії з базою даних
class Database:
    def get_data(self):
        return "Отримано дані з бази даних"

# Підсистема для обробки даних
class DataProcessor:
    def process_data(self, data):
        return f"Обробка даних: {data}"

# Підсистема для відображення результатів
class ResultsViewer:
    def view_results(self, results):
        return f"Відображення результатів: {results}"

# Фасад, який надає спрощений інтерфейс для використання підсистем
class Facade:
    def __init__(self):
        self.database = Database()
        self.processor = DataProcessor()
        self.viewer = ResultsViewer()

    def get_and_process_data(self):
        data = self.database.get_data()
        processed_data = self.processor.process_data(data)
        results = self.viewer.view_results(processed_data)
        return results

# Використання
if __name__ == "__main__":
    facade = Facade()
    result = facade.get_and_process_data()
    print(result)



"""
Патерн "Фасад" надає спрощений інтерфейс до складних систем, що дозволяє клієнтам легше з нею взаємодіяти.
"""
