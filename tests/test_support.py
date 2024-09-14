from src.support_functions import digit_or_special_present, is_empty_or_only_space, is_vowel
from src.support_functions import divide_vowels_consonants

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
    THEN: the function returns true only if the string is empty or only spaces
    """
    assert is_empty_or_only_space("ciao ") == False
    assert is_empty_or_only_space("") == True 
    assert is_empty_or_only_space(" ") == True

def test_is_vowel():
    """
    Test the is_vowel function.
    GIVEN: a single character
    WHEN: the function is called with a char
    THEN: the function returns true only if a char is ASCII vowel
    """
    
    assert is_vowel('a') == True
    assert is_vowel('A') == True
    assert is_vowel('b') == False

def test_divide_vowels_consonants():
    """
    Test the divide_vowels_consonants function.
    GIVEN: a string representing a word
    WHEN: the function is called with a word
    THEN: the function returns a string containing the vowels and one consonants
    """
    assert divide_vowels_consonants("ciao")[0] == "iao"
    assert divide_vowels_consonants("ciao")[1] == "c"
    assert divide_vowels_consonants("ciao")[0] + divide_vowels_consonants("ciao")[1] == "iaoc"
    assert divide_vowels_consonants("")[0] == ""
    assert divide_vowels_consonants("")[1] == ""
    assert divide_vowels_consonants("   ")[0] == ""
    assert divide_vowels_consonants("  ")[1] == ""
    assert divide_vowels_consonants("a  ")[0] == "a"
    assert divide_vowels_consonants("a  ")[1] == ""