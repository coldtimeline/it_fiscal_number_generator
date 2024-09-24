import sys
import os
import pytest
import pandas as pd
from datetime import datetime

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from src.support_functions import divide_vowels_consonants
from src.generate_functions import generate_day_gender_code, generate_name_code, generate_surname_code
from src.generate_functions import generate_month_char, generate_last_characther, generate_city_code
from src.generate_functions import generate_fiscal_code
from src.ask_functions import get_dataframe_from_html

def test_generate_day_gender_code_male():
    """
    Test the generate_day_gender_code function.
    GIVEN: a bool representing Male (true) and an int representing a day of birth
    WHEN: the function is called with above data
    THEN: the function returns the exact day of birth 
    """

    assert generate_day_gender_code(True, 15) == 15 


def test_generate_day_gender_code_female():
    """
    Test the generate_day_gender_code function.
    GIVEN: a bool a Female (false) and an int representing a day of birth
    WHEN: the function is called with above data
    THEN: the function returns the day of birth plus 40
    """
    assert generate_day_gender_code(False, 15) == 55  


def test_generate_name_and_surname_difference():
    """
    This function test that generate name and surname functions
    behave differently with more than 3 consonants
    GIVEN: the same consonat string with 4 consonant
    WHEN: generate_name_code and generate_surname_code are both called with above data
    THEN: the result are different
    """

    assert generate_name_code("","SDFG") != generate_surname_code("","SDFG")


def test_generate_name_code_lots_consonants():
    """
    Test the generate_name_code function
    GIVEN: a string of vowels and a string with more than 3 consonants
    WHEN: the function is called with above data
    THEN: the function returns a three char string according to roules
    """
    assert generate_name_code("AEI", "SDFQW") == "SFQ"

def test_generate_name_code_three_consonants():
    """
    Test the generate_name_code function 
    GIVEN: three consonants and some vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("AE", "SDF") == "SDF"

def test_generate_name_code_two_consonants_and_vowels():
    """
    Test the generate_name_code function
    GIVEN: with two consonants and some vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("AE", "SD") == "SDA"

def test_generate_name_code_two_consonants_no_vowels():
    """
    Test the generate_name_code function
    GIVEN: two consonants and no vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("", "LP") == "LPX"

def test_generate_name_code_one_consonant_two_vowels():
    """
    Test the generate_name_code function 
    GIVEN: one consonant and two vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("AE", "Q") == "QAE"

def test_generate_name_code_one_consonant_one_vowel():
    """
    Test the generate_name_code function 
    GIVEN: one consonant and one vowel
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("A", "B") == "BAX"

def test_generate_name_code_one_consonant_zero_vowels():
    """
    Test the generate_name_code function
    GIVEN: one consonant and zero vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("", "B") == "BXX"

def test_generate_name_code_zero_consonants_three_vowels():
    """
    Test the generate_name_code function
    GIVEN: zero consonants and three vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("AEI", "") == "AEI"

def test_generate_name_code_zero_consonants_two_vowels():
    """
    Test the generate_name_code function 
    GIVEN: zero consonants and two vowels
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("AE", "") == "AEX"

def test_generate_name_code_zero_consonants_one_vowel():
    """
    Test the generate_name_code function 
    GIVEN: zero consonants and one vowel
    WHEN: the function is called with above data
    THEN: the function returns three char string according to roules
    """
    assert generate_name_code("U", "") == "UXX"

def test_generate_name_code_empty():
    """
    Test the generate_name_code function 
    GIVEN: empty string for consonant and vowels
    WHEN: the function is called with above data
    THEN: the function raises ValueError
    """
    with pytest.raises(ValueError, match="Invalid input name"):
        generate_name_code("","")







    

def test_generate_surname_code_lot_of_consonants():
    """
    Test the generate_surname_code function
    GIVEN: lots of consonants and some vowel
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("AE", "BLTKJ") == "BLT"

def test_generate_surname_code_three_consonants():
    """
    Test the generate_surname_code function
    GIVEN: no vowels and  with three consonants
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("", "BLT") == "BLT"

def test_generate_surname_code_two_consonants_and_vowels():
    """
    Test the generate_surname_code function  
    GIVEN: two consonants and vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("AE", "BL") == "BLA"

def test_generate_surname_code_two_consonants_no_vowels():
    """
    Test the generate_surname_code function 
    GIVEN:  two consonants and no vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("", "BL") == "BLX"

def test_generate_surname_code_one_consonant_two_vowels():
    """
    Test the generate_surname_code function 
    GIVEN: one consonant and two vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("AE", "B") == "BAE"

def test_generate_surname_code_one_consonant_one_vowel():
    """
    Test the generate_surname_code function 
    GIVEN: one consonant and one vowel
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("A", "B") == "BAX"

def test_generate_surname_code_one_consonant_zero_vowels():
    """
    Test the generate_surname_code function 
    GIVEN: one consonant and zero vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("", "B") == "BXX"

def test_generate_surname_code_zero_consonants_three_vowels():
    """
    Test the generate_surname_code function 
    GIVEN: zero consonants and three vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("AEI", "") == "AEI"

def test_generate_surname_code_zero_consonants_two_vowels():
    """
    Test the generate_surname_code function 
    GIVEN: zero consonants and two vowels
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("AE", "") == "AEX"

def test_generate_surname_code_zero_consonants_one_vowel():
    """
    Test the generate_surname_code function 
    GIVEN: zero consonants and one vowel
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("U", "") == "UXX"

def test_generate_surname_code_zero_consonants_zero_vowels():
    """
    Test the generate_surname_code function
    GIVEN: no vowels and no consonants
    WHEN: the function is called with above data
    THEN: it should return three char string according to roules
    """
    assert generate_surname_code("", "") == "XXX"






def test_generate_month_char_valid():
    """ 
    Test the generate_month_char function.
    GIVEN: an integer between 1 and 12 inclusive
    WHEN: the function is called with a valid integer
    THEN: the function returns a char according to roules from Agenzia Entrate
    """
    assert generate_month_char(1) == 'A'
    assert generate_month_char(2) == 'B'
    assert generate_month_char(3) == 'C'
    assert generate_month_char(4) == 'D'
    assert generate_month_char(5) == 'E'
    assert generate_month_char(6) == 'H'
    assert generate_month_char(7) == 'L'
    assert generate_month_char(8) == 'M'
    assert generate_month_char(9) == 'P'
    assert generate_month_char(10) == 'R'
    assert generate_month_char(11) == 'S'
    assert generate_month_char(12) == 'T'

def test_generate_month_char_invalid():
    """ 
    Test the generate_month_char function.
    GIVEN: an invalid number
    WHEN: the function is called with an invalid integer
    THEN: the function raises ValueError
    """
    with pytest.raises(ValueError, match="Month must be between 1 and 12 inclusive."):
        generate_month_char(13)






def test_generate_last_characther_valid1():
    """
    Test the generate_last_characther function with a valid string
    GIVEN: the string 'GSTMGV78T03A944' with length 15
    WHEN: the function is called with that string
    THEN: the function returns the character 'T' according to the rules
    """
    assert generate_last_characther("GSTMGV78T03A944") == "T"

def test_generate_last_characther_valid2():
    """
    Test the generate_last_characther function with a valid string
    GIVEN: the string 'LTZCST80A41G712' with length 15
    WHEN: the function is called with 'LTZCST80A41G712'
    THEN: the function returns the character 'C' according to the rules
    """
    assert generate_last_characther("LTZCST80A41G712") == "C"

def test_generate_last_characther_shorter():
    """
    Test the generate_last_characther function with an invalid string
    GIVEN: a shorter input string, with 14 character
    WHEN: the function is called with that string
    THEN: the function raises ValueError
    """

    with pytest.raises(ValueError, match="Input code must have 15 characters"):
        generate_last_characther("GSTMGV78T3A944")





def test_generate_city_code():
    """
    This function test generate_city_code function when valid dataset and place is given

    GIVEN: the dataset of place and the correct name of a place
    WHEN: the function is called with those information
    THEN: it return the right code
    """
    dataset_from_html = get_dataframe_from_html('codici_comuni.htm')
    assert generate_city_code(dataset_from_html, "MONTECCHIO EMILIA") == 'F463'


    


def test_generate_fiscal_code():
    """
    This function test generate_fiscal_code when valid person is given

    GIVEN: place dataframe, a datetime object and data of a person
    WHEN: the function is called with a person with above characteristics
    THEN: it return a valid fiscal code according to roules
    """
    dataset_from_html = get_dataframe_from_html('codici_comuni.htm')
    datatest = datetime(1980, 1, 1)
    assert generate_fiscal_code('MARIA ROSA','BOCCIONI','F',datatest,'POMPEI',dataset_from_html) == 'BCCMRS80A41G813Y'


def test_generate_fiscal_code_singledigitday():
    """
    This function test generate_fiscal_code when a male with a sigle 
    digit day of birth

    GIVEN: a male with a one digit day of birth, a place dataframe
    WHEN: the function is called with a male with above characteristics
    THEN: it return a valid fiscal code according to roules
    """

    dataset_from_webpage = get_dataframe_from_html('codici_comuni.htm')
    data_test = datetime(1980, 1, 3)
    #this test tests if a man with only one digit for the day has two digit day in the fiscal code
    assert generate_fiscal_code('mario','rossi','m',data_test,'PISTICCI', dataset_from_webpage) == 'RSSMRA80A03G712K'
    