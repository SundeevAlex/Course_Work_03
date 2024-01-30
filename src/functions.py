import json


def load_operations(file_name):
    """
    Загружает список банковских операций из файла
    """
    with open(file_name, encoding='utf-8') as file:
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
    return sorted(data, key=key_sort, reverse=True)


def getting_operations_data(data):
    """
    Преобразовывает считанные из файла данные
    к отсортированному виду (по дате)
    """
    operations_data = operations_check(data)
    operations_data = sorted_operations_data(operations_data)
    return operations_data


def split_string(data):
    """
    Разбивка строки(информации об операции) на текстовую часть и цифровую
    """
    if data != '':
        from_name = ''
        from_number = ''
        split_data = data.split(' ')
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
    operation_amount = {"operationAmount": data[i]["operationAmount"]}
    amount = operation_amount["operationAmount"]["amount"]
    name = operation_amount["operationAmount"]["currency"]["name"]
    if "from" in data[i]:
        operation = {
            "date": data[i]["date"],
            "description": data[i]["description"],
            "from": data[i]["from"],
            "to": data[i]["to"],
            "amount": amount,
            "name": name
        }
    else:
        operation = {
            "date": data[i]["date"],
            "description": data[i]["description"],
            "to": data[i]["to"],
            "amount": amount,
            "name": name
        }
    return operation


def print_date_and_description(data):
    """
    Вывод на экран информации о дате и виде операции
    """
    date_of_operation = data["date"][:-16]
    date_of_operation = date_of_operation.split('-')
    date_of_operation = date_of_operation[2] + '.' + date_of_operation[1] + '.' + date_of_operation[0]
    print(date_of_operation, data["description"])
    return date_of_operation, data["description"]


def print_from_or_to_operation(data, direction, sign):
    """
    Вывод на экран информации откуда и куда была произведена операция
    """
    from_or_to_operation = data.get(direction, '')
    from_or_to_operation = split_string(from_or_to_operation)

    if from_or_to_operation is not None:
        if direction == 'from':
            from_or_to_number = from_or_to_operation[1][:4] + ' ' + from_or_to_operation[1][4:6] + '** **** ' + from_or_to_operation[1][-5:-1]
            print(from_or_to_operation[0][:-1], from_or_to_number, sign, end='')
        else:
            from_or_to_number = '**' + from_or_to_operation[1][-5:-1]
            print(from_or_to_operation[0][:-1], from_or_to_number, sign, end='')
        return from_or_to_number


def print_operation_amount(data):
    """
    Вывод на экран информации о сумме операции и в какой валюте это было произведено
    """
    print('\n' + data["amount"] + ' ' + data["name"] + '\n')
    return data["amount"] + ' ' + data["name"]


def print_all(data):
    """
    Вывод на экран всей информации об операциях совершенных клиентом банка
    (print_date_and_description, print_from_or_to_operation, print_operation_amount)
    """
    print_date_and_description(data)
    print_from_or_to_operation(data, "from", '-> ')
    print_from_or_to_operation(data, "to", '')
    return print_operation_amount(data)
