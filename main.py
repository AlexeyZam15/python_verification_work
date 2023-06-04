from core.infrastructure.notebook import Notebook


def main():
    notebook = Notebook()
    notebook.add('Проверка1', 'Тест1')
    notebook.add('Проверка2', 'Тест2')
    notebook.add('Проверка3', 'Тест4')
    notebook.show()


if __name__ == "__main__":
    main()
