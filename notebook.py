from note import Note


class Notebook:
    __max_id_width = 2
    __max_title_width = 5
    __fields = ['id', 'title', 'msg', 'last modified date']

    def __init__(self, name: str):
        self.__notes = list()
        self.__notes.append(Note(*self.__fields))
        self.__name = name

    def add_note(self, title: str, msg: str):
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

    def find_notes(self, field, value):
        notes = list(filter(lambda x: getattr(x, field) == value, self.__notes))
        notes.insert(0, Note(*self.__fields))
        text = ''
        for i in notes:
            text += f'{i.id:{self.__max_id_width}}|{i.title:{self.__max_title_width}}|{i.date_time}\n'
        return text

    @property
    def fields(self):
        return self.__fields
