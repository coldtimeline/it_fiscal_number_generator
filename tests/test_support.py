from it_fiscal_number_generator.src.support_functions import digit_or_special_present

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