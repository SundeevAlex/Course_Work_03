from src.functions import operations_check, sorted_operations_data


def test_operations_check():
    assert operations_check([]) == []
    assert operations_check(['id']) != []


def test_sorted_operations_data():
    assert sorted_operations_data([]) == []
    # assert sorted_operations_data(['id']) != []

