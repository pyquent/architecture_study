# Неправильно з дотриманням SRP
class Report:
    def generate_report(self):
        # Генерація звіту

    def save_to_file(self):
        # Збереження звіту до файлу

# Правильно з дотриманням SRP
class Report:
    def generate_report(self):
        # Генерація звіту

# Окремий клас для збереження звіту
class ReportSaver:
    def save_to_file(self, report):
        # Збереження звіту до файлу
