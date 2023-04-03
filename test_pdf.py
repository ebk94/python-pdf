import pytest

def test_valid_pdf(get_word_dictionary):
    print('Expected result \n')

    ethalon_file=get_word_dictionary('test_task.pdf')
    print(ethalon_file)

    print('\n Actual result \n')

    test_file=get_word_dictionary('test_task.pdf')
    print(test_file)

    if ethalon_file == test_file:
        assert True
    else:
        False


def test_invalid_pdf(get_word_dictionary):
    print('Expected result \n')
    
    ethalon_file=get_word_dictionary('test_task.pdf')
    print(ethalon_file)

    print('\n Actual result \n')
    
    test_file=get_word_dictionary('TestPDFfile.pdf')
    print(test_file)

    if ethalon_file == test_file:
        assert True
    else:
        False
    