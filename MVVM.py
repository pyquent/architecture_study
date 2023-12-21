class Model:
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data

class ViewModel:
    def __init__(self, model):
        self.model = model
        self.data = None

    def update_data(self):
        self.data = self.model.get_data()

class View:
    def __init__(self, view_model):
        self.view_model = view_model

    def display_data(self):
        data = self.view_model.data
        print(f"Displaying data: {data}")


data_model = Model("Hello, MVVM!")
view_model = ViewModel(data_model)
display_view = View(view_model)


view_model.update_data()
display_view.display_data()
