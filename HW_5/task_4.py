"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""
if __name__ == "__main__":
    string = str(input("ввод данных: "))
    new_string = []
    list_string = list(string)
    set_string = set(list_string)
    new_list_string = list(set_string)
    list_string.sort()
    new_list_string.sort()
    for symbol in new_list_string:
        count = 0
        for other_symbol in list_string:
            if symbol == other_symbol:
                count += 1
        new_string.append(symbol)
        new_string.append(str(count))
    new_string = ''.join(new_string)
    print(new_string)