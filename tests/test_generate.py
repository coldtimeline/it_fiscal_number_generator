import sys
import os
import pandas as pd
from datetime import datetime

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from src.support_functions import divide_vowels_consonants
from src.generate_functions import generate_day_gender_code, generate_name_code, generate_surname_code
from src.generate_functions import generate_month_char, generate_last_characther, generate_city_code
from src.generate_functions import generate_fiscal_code
from src.ask_functions import get_dataframe_from_webpage

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

def test_generate_last_characther():
    """ 
    Test the generate last character function.
    GIVEN: a string with length 15
    WHEN: the function is called with a 15 length string
    THEN: the function a char according to the roules
    """
    assert generate_last_characther("GSTMGV78T03A944") == "T"
    assert generate_last_characther("LTZCST80A41G712") == "C"
    assert generate_last_characther("PPPGNN80A42B602") == "G"
    assert generate_last_characther("XIXTIX85H01E438") == "N"

def test_generate_city_code():
    dataset_from_internet = get_dataframe_from_webpage('codici_comuni.htm')
    assert generate_city_code(dataset_from_internet, "MONTECCHIO EMILIA") == 'F463'


def test_generate_fiscal_code():
    """
    This function test generate_fiscal_code when valid person is given

    GIVEN: a male with a one digit day of birth
    WHEN: the function is called with a male with above characteristics
    THEN: it return a valid fiscal code
    """
    dataset_from_webpage = get_dataframe_from_webpage('codici_comuni.htm')
    datatest = datetime(1980, 1, 1)
    assert generate_fiscal_code('maRia Rosa','boCCIoni','F',datatest,'POMPEI',dataset_from_webpage) == 'BCCMRS80A41G813Y'


def test_generate_fiscal_code_singledigitday():
    """
    This function test generate_fiscal_code when a male with a sigle 
    digit day of birth

    GIVEN: a male with a one digit day of birth
    WHEN: the function is called with a male with above characteristics
    THEN: it return a valid fiscal code
    """

    dataset_from_webpage = get_dataframe_from_webpage('codici_comuni.htm')
    data_test = datetime(1980, 1, 3)
    #this test tests if a man with only one digit for the day has two digit day in the fiscal code
    assert generate_fiscal_code('mario','rossi','m',data_test,'PISTICCI', dataset_from_webpage) == 'RSSMRA80A03G712K'
