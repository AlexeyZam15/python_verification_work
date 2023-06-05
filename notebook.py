from note import Note


class Notebook:
    __max_id_width = 2
    __max_title_width = 5

    def __init__(self, name: str):
        self.__notes = list()
        self.__notes.append(Note('id', 'title', 'msg', 'last modified date'))
        self.__name = name

    def add(self, title: str, msg: str):
        note = Note(len(self.__notes), title, msg)
        self.__notes.append(note)
        self.__set_max_fields_width(note)

    @property
    def notes(self):
        return self.__notes

    @property
    def name(self):
        return self.__name

    def __set_max_fields_width(self, note: Note):
        if len(note.id) > self.__max_id_width:
            self.__max_id_width = len(note.id)
        if len(note.title) > self.__max_title_width:
            self.__max_title_width = len(note.title)

    def __str__(self):
        notes = ''
        for i in self.__notes:
            notes += f'{i.id:{self.__max_id_width}}|{i.title:{self.__max_title_width}}|{i.date_time}\n'
        return notes

    def csv_format(self):
        notes = ''
        for i in self.__notes:
            notes += f'{i.id};{i.title};{i.msg};{i.date_time}\n'
        return notes

