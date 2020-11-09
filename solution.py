
import os
import tempfile


class File:
    """Интерфейс для работы с файлами"""
    def __init__(self, file_path: str):
        if not isinstance(file_path, str):
            raise TypeError
        elif not os.path.isfile(file_path):
            with open(file_path, 'w'):
                pass
        self.__file_path = file_path

    def read(self) -> str:
        """Чтение из файла"""
        with open(self.__file_path) as file:
            file_read = file.read()
        return file_read

    def write(self, text: str) -> int:
        """Запись в файл"""
        with open(self.__file_path, 'w') as file:
            result = file.write(text)
        return result

    def __iter__(self):
        """Итератор"""
        self.__current = 0
        with open(self.__file_path) as file:
            self.__lines = file.readlines()
        self.__end = len(self.__lines)
        return self

    def __next__(self):
        """Итерация по строкам в файле"""
        if self.__current >= self.__end:
            raise StopIteration
        read_line = self.__lines[self.__current]
        self.__current += 1
        return read_line

    def __add__(self, other_file):
        """Складывает два файла"""
        text = self.read() + other_file.read()
        _, path = tempfile.mkstemp()
        new_file = File(path)
        new_file.write(text)
        return new_file

    def __str__(self) -> str:
        """Строковое представление возвращает путь к файлу"""
        return self.__file_path


path_to_file = 'some_filename'
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
file_obj.read()
print(file_obj.write('some text'))
file_obj.read()
print(file_obj.write('other text'))
file_obj.read()
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
print(file_obj_1.write('line 1\n'))
print(file_obj_2.write('line 2\n'))
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(new_file_obj)
for line in new_file_obj:
    print(line, end='')
