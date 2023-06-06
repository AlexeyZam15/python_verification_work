class View:

    def __init__(self, notebook):
        self.__notebook = notebook
        print(f'Программа Заметки запущена')

    def wait_action(self, actions, functions):
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        while action not in actions:
            print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
            action = input()
            if action not in actions:
                print('Введены неверные данные')
        if action == 'q':
            print('Программа Заметки завершена')
        else:
            functions[action]()
        return action

    @staticmethod
    def show_notes(txt):
        print(txt)

    def add_notes(self):
        print('Введите заголовок сообщения')
        title = input()
        print('Введите текст сообщения')
        msg = input()
        confirm = self.__confirmation('добавление')
        if confirm == 'y':
            return title, msg

    @staticmethod
    def __confirmation(text: str):
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
        while confirm not in ('y', 'n'):
            print('Введены неверные данные')
            confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
        return confirm

    @staticmethod
    def end(self):
        print('Программа Заметки заверщена')

    def find_field(self, fields: list):
        print('Выберите поле для поиска:')
        text = ''
        text = ', '.join([f'{i} - {fields[i]}' for i in range(len(fields))]) + ', q - выйти'
        choices = [str(i) for i in range(len(fields))]
        print(text)
        choice = input()
        while choice not in choices and choice != 'q':
            print('Введены неверные данные')
            print('Выберите характеристику:')
            print(text)
            choice = input()
        if choice != 'q':
            condition = input('Введите значение\n')
            return fields[int(choice)], condition
        else:
            return 'q', 'q'
