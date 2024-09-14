import sys
import os

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from src.support_functions import divide_vowels_consonants
from src.generate_functions import generate_day_gender_code, generate_name_code, generate_surname_code
from src.generate_functions import generate_month_char

def test_generate_day_gender_code():
    """
    Test the generate_day_gender_code function.
    GIVEN: a bool representing Male (true) or Female (false) and an int representing a day of birth
    WHEN: the function is called with a gender bool and the day of birth
    THEN: the function returns the day of birth if the gender is male, otherwise the day of birth plus 40
    """

    assert generate_day_gender_code(True, 15) == 15  # Male, should return the day of birth
    assert generate_day_gender_code(False, 15) == 55  # Female, should return the day of birth plus 40


def test_generate_name_code():
    """ 
    Test the generate_name_code function.
    GIVEN: two string representing vowels and consonats of a word, respectively
    WHEN: the function is called with two string, one of vowels and one of consonants
    THEN: the function returns a three char string of the name according to the rules
    """
    assert generate_name_code("AEI", "SDFQW") == "SFQ"  # Four or more consonants
    assert generate_name_code("AE", "SDF") == "SDF"  # Three consonants
    assert generate_name_code("AE", "SD") == "SDA"  # Two consonants and one vowel
    assert generate_name_code("", "LP") == "LPX"  # Two consonants and no vowels
    assert generate_name_code("AE", "Q") == "QAE"  # One consonants and two vowel
    assert generate_name_code("A", "B") == "BAX"  # One consonants and one vowel
    assert generate_name_code("", "B") == "BXX"  # One consonants and zero vowel
    assert generate_name_code("AEI", "") == "AEI"  # Zero consonants and three vowel
    assert generate_name_code("AE", "") == "AEX"  # Zero consonants and two vowel
    assert generate_name_code("U", "") == "UXX"  # Zero consonants and one vowel

    

def test_generate_surname_code():
    """ 
    Test the generate_surname_code function.
    GIVEN: two string representing vowels and consonats of a word, respectively
    WHEN: the function is called with two string, one of vowels and one of consonants
    THEN: the function returns a three char string of the surname according to the rules
    """
    assert generate_surname_code("", "BLTKJ") == "BLT"  # Lot of consonants
    assert generate_surname_code("AE", "BLTKJ") == "BLT"  # Lot of consonants
    assert generate_surname_code("", "BLT") == "BLT"  # Three consonants
    assert generate_surname_code("AE", "BL") == "BLA"  # Two consonants and one vowel
    assert generate_surname_code("", "BL") == "BLX"  # Two consonants and no vowels
    assert generate_surname_code("AE", "B") == "BAE"  # One consonants and two vowel
    assert generate_surname_code("AEUI", "B") == "BAE"  # One consonants and more vowel
    assert generate_surname_code("A", "B") == "BAX"  # One consonants and one vowel
    assert generate_surname_code("", "B") == "BXX"  # One consonants and zero vowel
    assert generate_surname_code("AEI", "") == "AEI"  # Zero consonants and three vowel
    assert generate_surname_code("AEI", "") == "AEI"  # lots of vowel
    assert generate_surname_code("AE", "") == "AEX"  # Zero consonants and two vowel
    assert generate_surname_code("U", "") == "UXX"  # Zero consonants and one vowel
    assert generate_surname_code("", "") == "XXX"  # Zero consonants and zero vowel
    assert generate_surname_code(divide_vowels_consonants("Rocchini")[0], divide_vowels_consonants("Rocchini")[1]) == "RCC"



def test_generate_month_char():
    """ 
    Test the generate_month_char function.
    GIVEN: an integer between 1 and 12 inclusive
    WHEN: the function is called with a integer
    THEN: the function returns a three char string of the surname according to the rules
    """
    assert generate_month_char(1) == 'A'
    assert generate_month_char(5) == 'E'
    assert generate_month_char(9) == 'P'
    assert generate_month_char(2) == 'B'
    assert generate_month_char(6) == 'H'
    assert generate_month_char(10) == 'R'
    assert generate_month_char(3) == 'C'
    assert generate_month_char(7) == 'L'
    assert generate_month_char(11) == 'S'
    assert generate_month_char(4) == 'D'
    assert generate_month_char(8) == 'M'
    assert generate_month_char(12) == 'T'