class View:

    def __init__(self):
        print(f'Программа Заметки запущена')

    def wait_action(self):
        actions = {'1': 'чтение',
                   '2': 'запись',
                   '3': 'поиск',
                   '4': 'изменение',
                   '5': 'удаление',
                   'q': 'выход'}

        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        while action not in actions:
            print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
            action = input()
            if action not in actions:
                print('Введены неверные данные')
        if action == 'q':
            print('Программа Заметки завершена')
        return action

    def show_notes(self):
        print(self.__notebook)

    def add_notes(self):
        print('Введите заголовок и тело сообщения через пробел')
        note = input()
        return note

    def end(self):
        print('Программа Заметки заверщена')
