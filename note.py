from abc import abstractmethod
import datetime


class Note:
    field = ''

    def __init__(self, id_counter, title: str, msg: str,
                 date_time=datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S")):
        self.__id = str(id_counter)
        self.__title = title
        self.__msg = msg
        self.__date_time = date_time

    def __str__(self):
        return f'{self.__id}|{self.__title}|{self.__date_time}'

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def msg(self):
        return self.__msg

    @property
    def date_time(self):
        return self.__date_time
