from src.support_functions import digit_or_special_present, is_empty_or_only_space

def test_digit_or_special_present():
    """
    This tests that the test_digit_or_special_present function 
    correctly checks if digit or punctation are present.

    GIVEN: string with or without digit and punctation
    WHEN: the function is called with a string
    THEN: the function returns true only if digit or punctation is present
    """
    assert digit_or_special_present("ciao") == False #alphabet string
    assert digit_or_special_present("ciao1") == True #string with digits
    assert digit_or_special_present("ciao!") == True #string with punctation
    assert digit_or_special_present("") == False #empty string
    assert digit_or_special_present(" ") == False #string with spaces

def test_is_empty_or_only_space():
    """
    Test the is_empty_or_only_space function.
    GIVEN: empty or spaces or non empty string
    WHEN: the function is called with a string
    THEN: the function returns true only if digit or punctation is present
    """
    assert is_empty_or_only_space("ciao ") == False
    assert is_empty_or_only_space("") == True 
    assert is_empty_or_only_space(" ") == True

