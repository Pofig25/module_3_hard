def calculate_structure_sum(data_structure):        # создаём функцию
    sum = 0                                         # создаём переменную для записи результатов суммирования

    if isinstance(data_structure, int):             # если целые числа
        sum += data_structure                       # суммируем

    if isinstance(data_structure, float):           # если дробные числа
        sum += data_structure                       # суммируем

    if isinstance(data_structure, str):             # если строка
        sum += len(data_structure)                  # суммируем длину строки

    if isinstance(data_structure, list):            # если список
        for i in data_structure:                    # перебираем элементы списка
            sum += calculate_structure_sum(i)       # и суммируем их количество

    if isinstance(data_structure, tuple):           # если кортеж
        for i in data_structure:                    # перебираем элементы кортежа
            sum += calculate_structure_sum(i)       # и суммируем их количество

    if isinstance(data_structure, set):             # если множество
        for i in data_structure:                    # перебираем элементы множества
            sum += calculate_structure_sum(i)       # и суммируем их количество

    if isinstance(data_structure, dict):            # если словарь
        for key, value in data_structure.items():   # перебираем элементы ключ и значение
            sum += calculate_structure_sum(key)     # суммируем ключи
            sum += calculate_structure_sum(value)   # суммируем значения

    return sum                                      # возвращаем переменную

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])] # исходные данные

result = calculate_structure_sum(data_structure)
print(result)