from functions import load_operations, operations_check, sorted_operations_data


def main():
    operations_data = load_operations('operations.json')
    operations_data = operations_check(operations_data)
    operations_data = sorted_operations_data(operations_data)

    for i in range(3):
        if "from" in operations_data[i]:
            operation = {
                "date": operations_data[i]["date"],
                "description": operations_data[i]["description"],
                "from": operations_data[i]["from"],
                "to": operations_data[i]["to"],
            }
        else:
            operation = {
                "date": operations_data[i]["date"],
                "description": operations_data[i]["description"],
                "to": operations_data[i]["to"],
            }

        date_of_operation = operation["date"][:-16]
        date_of_operation = date_of_operation.split('-')
        date_of_operation = date_of_operation[2] + '.' + date_of_operation[1] + '.' + date_of_operation[0]

        print(date_of_operation, operation["description"])
        from_operation = operation.get('from', '') + ' '
        to_operation = operation["to"] + ' '

        from_operation_number = from_operation[-16:-1]
        to_operation_number = to_operation
        print('number-', to_operation)
        if from_operation != ' ':
            from_operation_number = from_operation_number[:4] + ' ' + from_operation_number[4:6] + '** **** ' + from_operation_number[11:16]
            print(from_operation[0:-18], from_operation_number, '->', to_operation[0:-17], '**', to_operation[-5:-1])

        print('')


if __name__ == '__main__':
    main()
