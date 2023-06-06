from note import Note
import datetime


class Notebook:
    __fields = {'id': 4, 'title': 30, 'msg': 60, 'creation_date': 25, 'last_change_date': 25}

    def __init__(self, name: str):
        self.__notes = list()
        self.__notes.append(Note(*list(self.__fields.keys())[:3]))
        self.__notes[0].creation_date = 'creation date'
        self.__notes[0].last_change_date = 'last change date'
        self.__name = name

    def add_note(self, title: str, msg: str):
        note = Note(len(self.__notes), title, msg)
        self.__notes.append(note)

    @property
    def notes(self):
        return self.__notes

    @property
    def name(self):
        return self.__name

    def __str__(self):
        notes = ''
        for i in self.__notes:
            notes += '|'.join([f'{getattr(i, j)[:self.fields[j]]:{self.fields[j]}}' for j in self.__fields])
            notes += '\n'
        # for i in self.__notes:
        #     notes += f'{i.id:{self.__max_id_width}}|{i.title:{self.__max_title_width}}|{i.creation_date}\n'
        return notes

    def csv_format(self):
        notes = ''
        for i in self.__notes:
            notes += ';'.join([f'{getattr(i, j)}' for j in self.__fields])
            notes += '\n'
        return notes

    def find_notes(self, field, value):
        temp_notebook = Notebook('Временный')
        temp_notebook.__notes += list(filter(lambda x: value in getattr(x, field), self.__notes))
        return temp_notebook

    @property
    def fields(self):
        return self.__fields

    def change_note(self, id_note, field, value):
        setattr(self.__notes[id_note], field, value)
        self.__notes[id_note].last_change_date = datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S")

    def __len__(self):
        return len(self.__notes) - 1
