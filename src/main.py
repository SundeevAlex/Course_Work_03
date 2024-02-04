from functions import load_operations, get_operation, getting_operations_data, print_all


def main():
    operations_data = load_operations('operations.json')
    operations_data = getting_operations_data(operations_data)

    for i in range(3):
        operation = get_operation(operations_data, i)
        print_all(operation)


if __name__ == '__main__':
    main()
