from abc import abstractmethod
import datetime


class Note:

    def __init__(self, id_counter, title: str, body: str):
        self.__id = id_counter
        self.__title = title
        self.__body = body
        self.__date_time = datetime.datetime.today()
        self.__date_time = self.__date_time.strftime("%d-%b-%Y %H:%M:%S")

    def __str__(self):
        return f'{self.__id:4}|{self.__title:4}|{self.__body:4}|{self.__date_time}'

