from src.functions import operations_check


def test_operations_check():
    assert operations_check([]) == []
    assert operations_check(['id']) != []

