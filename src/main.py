from functions import load_operations, operations_check, sorted_operations_data


def main():
    operations_data = load_operations('operations_lit.json')
    operations_data = operations_check(operations_data)
    operations_data = sorted_operations_data(operations_data)

    for el in operations_data:
        print(el)

#  s = s[::-1]


if __name__ == '__main__':
    main()
