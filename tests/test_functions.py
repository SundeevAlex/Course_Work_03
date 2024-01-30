import pytest
from src.functions import operations_check, sorted_operations_data, get_operation
from src.functions import load_operations, split_string, print_date_and_description
from src.functions import print_from_or_to_operation, print_operation_amount, key_sort
from src.functions import print_all


def test_operations_check():
    assert operations_check([]) == []
    assert operations_check(['id']) != []


def test_sorted_operations_data():
    assert sorted_operations_data([]) == []


def test_get_operation():
    assert (get_operation([
        {'id': 863064926,
         'state': 'EXECUTED',
         'date': '2019-12-08T22:46:21.935582',
         'operationAmount':
             {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада',
         'from': "Maestro 1596837868705199",
         'to': 'Счет 90424923579946435907'}
    ], 0) == {
                'date': '2019-12-08T22:46:21.935582',
                'description': 'Открытие вклада',
                'from': 'Maestro 1596837868705199',
                'to': 'Счет 90424923579946435907',
                'amount': '41096.24',
                'name': 'USD'
            })
    assert (get_operation([
        {'id': 863064926,
         'state': 'EXECUTED',
         'date': '2019-12-08T22:46:21.935582',
         'operationAmount':
             {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада',
         'to': 'Счет 90424923579946435907'}
    ], 0) == {
                'date': '2019-12-08T22:46:21.935582',
                'description': 'Открытие вклада',
                'to': 'Счет 90424923579946435907',
                'amount': '41096.24',
                'name': 'USD'
            })


def test_get_operation__error():
    with pytest.raises(Exception):
        get_operation({})


def test_load_operations_err():
    with pytest.raises(Exception):
        load_operations('')


def test_split_string():
    assert split_string('Visa Classic 345345') == ['Visa Classic ', '345345 ']
    assert split_string('MasterCard 1796816785869527') == ['MasterCard ', '1796816785869527 ']
    assert split_string('Visa Classic card 555') == ['Visa Classic card ', '555 ']


def test_print_date_and_description():
    assert print_date_and_description(
        {'date': '2019-12-07T06:17:14.634890',
         'description': 'Перевод организации',
         'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'}) == ('07.12.2019', 'Перевод организации')


def test_print_from_or_to_operation():
    assert print_from_or_to_operation(
        {'from': 'Visa Classic 2842878893689012'}, 'from', '->') == '2842 87** **** 9012'
    assert print_from_or_to_operation(
        {'to': 'Master 2842878893689015'}, 'to', '') == '**9015'


def test_print_operation_amount():
    assert print_operation_amount(
        {
            'amount': '17628.50',
            'name': 'USD'
        }) == '17628.50 USD'
    assert print_operation_amount(
        {
            'amount': '17000.50',
            'name': 'руб.'
        }) == '17000.50 руб.'


def test_key_sort():
    assert key_sort({'id': 179194306, 'date': '2019-05-19T12:51:49.023880'}) == '2019-05-19T12:51:49.023880'
    assert key_sort({'id': 179194306, 'date': '2019-05-19T12:51:49.023880', 'description': 'Перевод организации'}) == '2019-05-19T12:51:49.023880'


def test_print_all():
    assert print_all(
        {'date': '2019-12-03T04:27:03.427014', 'description': 'Перевод с карты на карту',
         'from': 'MasterCard 1796816785869527', 'to': 'Visa Classic 7699855375169288', 'amount': '17628.50',
         'name': 'USD'}
    ) == '17628.50 USD'
