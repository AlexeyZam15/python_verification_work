class WorkWithFiles:

    def __init__(self, file_name: str):
        self.__file_name = file_name

    def save(self, text):
        with open(self.__file_name, 'w', encoding='utf-8') as data:
            data.write(str(text))
