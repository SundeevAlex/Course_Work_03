from functions import load_operations, operations_check, sorted_operations_data
from functions import get_operation, print_date_and_description
from functions import print_from_or_to_operation, print_operation_amount


def main():
    operations_data = load_operations('operations.json')
    operations_data = operations_check(operations_data)
    operations_data = sorted_operations_data(operations_data)

    for i in range(3):
        operation = get_operation(operations_data, i)

        print_date_and_description(operation)

        print_from_or_to_operation(operation, "from", '-> ')

        print_from_or_to_operation(operation, "to", '')

        print_operation_amount(operation)


if __name__ == '__main__':
    main()
