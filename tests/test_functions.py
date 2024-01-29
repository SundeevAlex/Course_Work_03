import pytest
from src.functions import operations_check, sorted_operations_data, get_operation
from src.functions import load_operations, split_string


def test_operations_check():
    assert operations_check([]) == []
    assert operations_check(['id']) != []


def test_sorted_operations_data():
    assert sorted_operations_data([]) == []
    # assert sorted_operations_data(['id']) != []


def test_get_operation():
    assert get_operation([
        {"date": "2019-08-26T10:50:58.294041",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589",
         "description": "Перевод организации"}
    ], 0) == {'date': '2019-08-26T10:50:58.294041',
              'description': 'Перевод организации',
              'from': 'Maestro 1596837868705199',
              'to': 'Счет 64686473678894779589'}


def test_get_operation__error():
    with pytest.raises(Exception):
        get_operation({})


def test_load_operations():
    with pytest.raises(Exception):
        load_operations('')


def test_split_string():
    assert split_string('Visa Classic 345345') == ['Visa Classic ', '345345']
    assert split_string('MasterCard 1796816785869527') == ['MasterCard ', '1796816785869527']
    assert split_string('Visa Classic card 555') == ['Visa Classic card ', '555']
