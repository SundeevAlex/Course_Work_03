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
