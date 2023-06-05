from notebook import Notebook
from view import View


def main():
    notebook = Notebook('Тест')
    view = View(notebook)
    notebook.add('Проверка1', 'Тест1')
    notebook.add('Проверка2', 'Тест2')
    notebook.add('45345435345345', 'Тест4')
    view.start()
    view.show_notes()


if __name__ == "__main__":
    main()
