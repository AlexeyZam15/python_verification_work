from notebook import Notebook
from view import View
from work_with_files import WorkWithFiles


class App:
    def __init__(self):
        self.__filename = 'заметки.csv'
        self.__notebook = Notebook('Тест')
        self.__view = View(self.__notebook)
        self.__work_with_files = WorkWithFiles(self.__filename)

    def start(self):

        # notebook = Notebook('Тест')
        # view = View(notebook)
        # notebook.add('Проверка1', 'Тест1')
        # notebook.add('Проверка2', 'Тест2')
        # notebook.add('45345435345345', 'Тест4')
        # view.start()
        # view.show_notes()
        # work_with_files = WorkWithFiles('Заметки.csv')
        # work_with_files.save(notebook.csv_format())

        try:
            file = open(self.__filename, 'r')
        except IOError:
            file = open(self.__filename, 'w')
        finally:
            file.close()

        actions = {'1': 'чтение',
                   '2': 'запись',
                   '3': 'поиск',
                   '4': 'изменение',
                   '5': 'удаление',
                   'q': 'выход'}

        functions = {'1': self.show_notes,
                     '2': self.add_notes,
                     '3': self.find_notes,
                     }
        # '4': view.change_notes,
        # '5': view.delete_notes

        action = None
        while action != 'q':
            self.__work_with_files.save(self.__notebook.csv_format())
            action = self.__view.wait_action(actions, functions)
            # if action != 'q':
            #     functions[action]()

    def show_notes(self):
        self.__view.show_notes(self.__notebook)

    def add_notes(self):
        self.__notebook.add_note(*self.__view.add_notes())

    def find_notes(self):
        field, value = self.__view.find_field(self.__notebook.fields)
        if field != 'q':
            self.__view.show_notes(self.__notebook.find_notes(field, value))

