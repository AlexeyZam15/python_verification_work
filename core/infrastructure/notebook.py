from core.models.note import Note


class Notebook:

    def __init__(self):
        self.__notes = list()

    def add(self, title: str, body: str):
        self.__notes.append(Note(len(self.__notes), title, body))

    def show(self):
        print(*self.__notes, sep='\n')
