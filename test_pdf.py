import pytest

def test_valid_pdf(get_word_dictionary):
    ethalon_file=get_word_dictionary('test_task.pdf')
    print(ethalon_file)

    test_file=get_word_dictionary('test_task.pdf')
    print(test_file)

    if ethalon_file == test_file:
        assert True
    else:
        False


def test_invalid_pdf(get_word_dictionary):
    ethalon_file=get_word_dictionary('test_task.pdf')
    print(ethalon_file)

    test_file=get_word_dictionary('TestPDFfile.pdf')
    print(test_file)

    if ethalon_file == test_file:
        assert True
    else:
        False
    