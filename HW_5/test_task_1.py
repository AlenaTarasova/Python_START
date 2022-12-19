import unittest

from task_1 import < str = str(input("ВВедите слова: "))
print(str.translate({ord(i): None for i in 'абв'})) > as target


# Класс с тестами
class TestClass(unittest.TestCase):

    def test_decode(self):
        """
        Метод тестирования функции по удалению слов, содержаших определенные буквы.
        Функция принимает первым аргументом текст, а вторым строку из букв.
        """

        # Если ваши полиномы не имеют пробелов, то уберите их в строках ниже.
        arg = 'автобус, генерал швабра итог арбуз вагон', 'абв'
        expect = 'генерал итог арбуз вагон'
        self.assertEqual(target(*arg), expect)


if __name__ == '__main__':
    unittest.main()
