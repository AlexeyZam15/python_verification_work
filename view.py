from notebook import Notebook


class View:

    def __init__(self, notebook: Notebook):
        self.__notebook = notebook
        print(f'Программа Заметки запущена')

    @staticmethod
    def wait_action(actions, functions):
        action = None
        while action not in actions:
            print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
            action = input()
            if action not in actions:
                print('Введены неверные данные')
        if action == 'q':
            print('Программа Заметки завершена')
        else:
            action = functions[action]()
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
        print("Введите текст сообщения. q - сохранить")
        msg = []
        line = ''
        while line != 'q':
            line = input()
            if line != 'q':
                msg.append(line)
        msg = '\\n'.join(msg)
        confirm = self.confirmation('Подтвердите добавление записи')
        if confirm:
            return title, msg
        return 'q', 'q'

    @staticmethod
    def confirmation(text: str):
        confirm = input(f"{text} y - да, n - нет\n")
        while confirm not in ('y', 'n'):
            print('Неправильный ввод')
            confirm = input(f"{text}: y - да, n - нет\n")
        return True if confirm == 'y' else False

    @staticmethod
    def end(self):
        print('Программа Заметки заверщена')

    @staticmethod
    def find_field(fields: list, action_word: str):
        text = ''
        text = ', '.join([f'{i} - {fields[i]}' for i in range(len(fields))]) + ', q - выйти'
        choices = [str(i) for i in range(len(fields))]
        choice = None
        while choice not in choices and choice != 'q':
            print(f'Выберите поле для {action_word}:')
            print(text)
            choice = input()
            if choice not in choices and choice != 'q':
                print('Неправильный ввод')
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
