from notebook import Notebook
from view import View
from work_with_files import WorkWithFiles


class App:
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

        path = 'notes.csv'
        notebook = Notebook('Тест')
        view = View(notebook)
        work_with_files = WorkWithFiles('Заметки.csv')

        try:
            file = open(path, 'r')
        except IOError:
            file = open(path, 'w')
        finally:
            file.close()

        functions = {'1': view.show_notes,
                     '2': view.add_notes,
                     }
        # '3': view.find_notes_default,
        # '4': view.change_notes,
        # '5': view.delete_notes

        action = None
        while action != 'q':
            work_with_files.save(notebook.csv_format())
            action = view.wait_action()
            if action != 'q':
                functions[action]()
