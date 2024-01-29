import json


def load_operations(file_name):
    """
    Загружает список банковских операций из файла
    """
    with open(file_name, encoding='utf-8') as file:
        # content = file.read()
        operations = json.loads(file.read())
    return operations


def operations_check(data):
    """
    Удаляет пустые строки из списка словарей
    """
    operations_data = []
    for el in data:
        if el != {}:
            operations_data.append(el)
    return operations_data


def key_sort(item):
    """
    Выбор нужного ключа по которому будет произведена сортировка
    """
    return item['date']


def sorted_operations_data(data):
    """
    Сортировка банковский операций по дате убывания
    """
    # operations_data_sorted = sorted(operations_data, key=lambda item: item["date"])
    return sorted(data, key=key_sort, reverse=True)


def split_string(data):
    """
    Разбивка строки на текстовую часть и цифровую
    """
    if data != '':
        from_name = ''
        from_number = ''
        split_data = data.split(' ')
        # print(split_data)
        for el in split_data:
            if el.isalpha():
                from_name += el + ' '
            else:
                from_number = el + ' '
        return [from_name, from_number]


def get_operation(data, i):
    """
    Получение необходимых полей для вывода
    """
    if "from" in data[i]:
        operation = {
            "date": data[i]["date"],
            "description": data[i]["description"],
            "from": data[i]["from"],
            "to": data[i]["to"],
        }
    else:
        operation = {
            "date": data[i]["date"],
            "description": data[i]["description"],
            "to": data[i]["to"],
        }
    return operation


def print_date_and_description(data):
    date_of_operation = data["date"][:-16]
    date_of_operation = date_of_operation.split('-')
    date_of_operation = date_of_operation[2] + '.' + date_of_operation[1] + '.' + date_of_operation[0]
    print(date_of_operation, data["description"])
    return date_of_operation, data["description"]


def print_from_or_to_operation(data, direction, sign):
    from_or_to_operation = data.get(direction, '')
    # to_operation = operation["to"] + ' '
    # print(from_operation)
    from_or_to_operation = split_string(from_or_to_operation)

    if from_or_to_operation is not None:
        if direction == 'from':
            from_or_to_number = from_or_to_operation[1][:4] + ' ' + from_or_to_operation[1][4:6] + '** **** ' + from_or_to_operation[1][-5:-1]
            # print(from_operation[0][:-1], from_number, '->')
            print(from_or_to_operation[0][:-1], from_or_to_number, sign, end='')
        else:
            from_or_to_number = '**' + from_or_to_operation[1][-5:-1]
            print(from_or_to_operation[0][:-1], from_or_to_number, sign, end='')
        return from_or_to_number
