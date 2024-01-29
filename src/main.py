from functions import load_operations, operations_check, sorted_operations_data
from functions import split_string, get_operation


def main():
    operations_data = load_operations('operations.json')
    operations_data = operations_check(operations_data)
    operations_data = sorted_operations_data(operations_data)

    for i in range(3):
        operation = get_operation(operations_data, i)
        # operations_data = [
        #     {"date": "2019-08-26T10:50:58.294041",
        #      "from": "Maestro 1596837868705199",
        #      "to": "Счет 64686473678894779589",
        #      "description": "Перевод организации"}
        # ]
        # print('входные', operations_data)
        # operation = get_operation(operations_data, 0)
        # print('выходные', operation)

        date_of_operation = operation["date"][:-16]
        date_of_operation = date_of_operation.split('-')
        date_of_operation = date_of_operation[2] + '.' + date_of_operation[1] + '.' + date_of_operation[0]
        print(date_of_operation, operation["description"])
        #
        # from_operation = operation.get("from", '') + ' '
        # print(from_operation)
        # split_string(from_operation)

        # from_operation = operation.get('from', '') + ' '
        # to_operation = operation["to"] + ' '
        #
        # from_operation_number = from_operation[-16:-1]
        # to_operation_number = to_operation
        # print('number-', to_operation)
        # if from_operation != ' ':
        #     from_operation_number = from_operation_number[:4] + ' ' + from_operation_number[4:6] + '** **** ' + from_operation_number[11:16]
        #     print(from_operation[0:-18], from_operation_number, '->', to_operation[0:-17], '**', to_operation[-5:-1])
        #
        print('')


if __name__ == '__main__':
    main()
