from notebook import Notebook


class View:

    def __init__(self, notebook: Notebook):
        self.__notebook = notebook
        print(f'Программа Заметки запущена')

    @staticmethod
    def wait_action(actions, functions):
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
    def show_notes(notes):
        if notes:
            print(notes)
        else:
            print('Записей не найдено')

    def add_notes(self):
        print('Введите заголовок сообщения')
        title = input()
        print('Введите текст сообщения')
        msg = input()
        confirm = self.confirmation('Подтвердите добавление записи')
        if confirm:
            return title, msg

    @staticmethod
    def confirmation(text: str):
        confirm = input(f"{text} y - да, n - нет\n")
        while confirm not in ('y', 'n'):
            print('Введены неверные данные')
            confirm = input(f"{text}: y - да, n - нет\n")
        return True if confirm == 'y' else False

    @staticmethod
    def end(self):
        print('Программа Заметки заверщена')

    @staticmethod
    def find_field(fields: list, action_word: str):
        print(f'Выберите поле для {action_word}:')
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

    def check_id_note(self, action_word: str):
        confirm = False
        id_note = ''
        while not confirm:
            id_note = input(f'Введите id записи которую хотите {action_word}, q - отмена\n')
            while id_note != 'q' and not self.__notebook.find_notes('id', id_note):
                print('Записей с таким id нет')
                id_note = input(f'Введите id записи которую хотите {action_word}, q - отмена\n')
            if id_note == 'q':
                return id_note
            self.show_notes(self.__notebook.find_notes('id', id_note))
            confirm = self.confirmation(f'Вы хотите {action_word} данную запись?')
        return id_note
