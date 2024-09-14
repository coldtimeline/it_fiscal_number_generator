import sys
import os

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))



from src.support_functions import digit_or_special_present, is_empty_or_only_space, is_vowel
from src.support_functions import divide_vowels_consonants, is_name_ok, is_surname_ok, is_gender_ok
from src.support_functions import is_place_of_birth_ok, gender_to_boolean, last_two_digits, even_position_to_number

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



def test_is_name_ok():
    """
    Test the is_name_ok function.
    GIVEN: a string representing a name
    WHEN: the function is called with a name
    THEN: the function returns true only no punctation is present, no digit is present
    and no non ASCII character is present, and if it is not empty or only spaces
    """
    assert  is_name_ok('cate')==True
    assert  is_name_ok('cate5')==False
    assert  is_name_ok('')==False
    assert  is_name_ok('    ')==False
    assert  is_name_ok('gianmar.ia')==False #because i don't know where to divide it
    assert  is_name_ok('gian maria')==True
    assert  is_name_ok(' gian maria')==True
    assert  is_name_ok('gian marià ')==False #name with accent

def test_is_surname_ok():
    """
    Test the is_surname_ok function.
    GIVEN: a string representing a surname
    WHEN: the function is called with a surname
    THEN: the function returns true only no punctation is present, no digit is present
    and no non ASCII character is present, but also if is empty or only spaces
    """
    assert  is_surname_ok('cate')==True
    assert  is_surname_ok('cate5')==False
    assert  is_surname_ok('')==True
    assert  is_surname_ok('    ')==True
    assert  is_surname_ok('bianchi.rossi')==False
    assert  is_surname_ok('bianchi rossi')==True
    assert  is_surname_ok(' bianchi rossi')==True
    assert  is_surname_ok('bianchi rossè ')==False #non ASCII


def test_is_gender_ok():
    """
    Test the is_gender_ok function.
    GIVEN: a string representing a gender
    WHEN: the function is called with a gender string
    THEN: the function returns true only if the string is M or m or F or f
    """
    assert is_gender_ok('M') == True
    assert is_gender_ok('m') == True
    assert is_gender_ok('F') == True
    assert is_gender_ok('f') == True
    assert is_gender_ok('maschio') == False

def test_is_place_of_birth_ok():
    """
    Test the is_place_of_birth_ok function.
    GIVEN: a string representing a place of birth
    WHEN: the function is called with a place of birth string
    THEN: the function returns true only if the string is not empty or only spaces
    and no digit are present
    """
    assert is_place_of_birth_ok('Roma') == True
    assert is_place_of_birth_ok('Roma2') == False
    assert is_place_of_birth_ok('') == False
    assert is_place_of_birth_ok('   ') == False


def test_gender_to_boolean():
    """
    Test the gender_to_boolean function.
    GIVEN: a char representing a gender
    WHEN: the function is called with a gender char
    THEN: the function returns true only if the string is M or m
    """
    assert gender_to_boolean('M') == True
    assert gender_to_boolean('m') == True
    assert gender_to_boolean('F') == False
    assert gender_to_boolean('f') == False


def test_last_two_digits():
    """
    Test the last_two_digits function.
    GIVEN: an integer number
    WHEN: the function is called with a number
    THEN: the function returns the last two digits of the number
    """
    assert last_two_digits(2023) == '23'
    assert last_two_digits(1980) == '80'
    assert last_two_digits(1979) == '79'
    assert last_two_digits(5) == '05'
    assert last_two_digits(0) == '00'
    assert last_two_digits(2000) == '00'


def test_even_position_to_number():
    assert even_position_to_number("A") == 0
    assert even_position_to_number("B") == 1
    assert even_position_to_number("C") == 2
    assert even_position_to_number("D") == 3
    assert even_position_to_number("E") == 4
    assert even_position_to_number("F") == 5
    assert even_position_to_number("G") == 6
    assert even_position_to_number("H") == 7
    assert even_position_to_number("I") == 8
    assert even_position_to_number("J") == 9
    assert even_position_to_number("K") == 10
    assert even_position_to_number("L") == 11
    assert even_position_to_number("M") == 12
    assert even_position_to_number("N") == 13
    assert even_position_to_number("O") == 14
    assert even_position_to_number("P") == 15
    assert even_position_to_number("Q") == 16
    assert even_position_to_number("R") == 17
    assert even_position_to_number("S") == 18
    assert even_position_to_number("T") == 19
    assert even_position_to_number("U") == 20
    assert even_position_to_number("V") == 21
    assert even_position_to_number("W") == 22
    assert even_position_to_number("X") == 23
    assert even_position_to_number("Y") == 24
    assert even_position_to_number("Z") == 25
    assert even_position_to_number("3") == 3