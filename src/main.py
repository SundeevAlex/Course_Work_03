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
            }
        else:
            operation = {
                "date": operations_data[i]["date"],
                "description": operations_data[i]["description"],
            }

        date_of_operation = operation["date"][:-16]
        date_of_operation = date_of_operation.split('-')
        date_of_operation = date_of_operation[2] + '.' + date_of_operation[1] + '.' + date_of_operation[0]

        print(date_of_operation, operation["description"])
        from_operation = operation.get('from', '-') + ' -> '
        # print(from_operation)
        if from_operation[0] != '-':
            from_operation_number = from_operation[-20:-1]
            from_operation_number = from_operation_number[:4] + ' ' + from_operation_number[5:7] + '** ****' + from_operation_number[14:17]
            print(from_operation[0:-21], from_operation_number)
        else:
            print(from_operation)
        # if from_operation != '-':
        #     from_operation1 = from_operation[-16:-1]
        # else:
        #     from_operation1 = from_operation
        # print(from_operation)

        print('')
        # for el in operations_data:
        #     print(el["id"])


if __name__ == '__main__':
    main()
