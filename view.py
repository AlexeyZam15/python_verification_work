class View:

    def __init__(self, notebook):
        self.__notebook = notebook

    def start(self):
        print(f'Программа Заметки запущена\nТекущая книга заметок: {self.__notebook.name}')

    def show_notes(self):
        print(self.__notebook)
