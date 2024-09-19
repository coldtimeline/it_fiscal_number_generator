import sys
import os

#add path to import modules
#add to the list of sys.path the path of the parent folder (the absolute path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))



from src.support_functions import digit_or_special_present, is_empty_or_only_space, is_vowel
from src.support_functions import divide_vowels_consonants, is_name_ok, is_surname_ok, is_gender_ok
from src.support_functions import is_place_of_birth_ok, gender_to_boolean, last_two_digits, even_position_to_number

def test_digit_or_special_present_alphabetic():
    """
    Test the digit_or_special_present function
    GIVEN: an alphabetic string
    WHEN: the function is called with an alphabetic string
    THEN: the function returns False
    """
    assert digit_or_special_present("ciao") == False

def test_digit_or_special_present_digits():
    """
    Test the digit_or_special_present function
    GIVEN: a string containing digits
    WHEN: the function is called with this string
    THEN: the function returns True
    """
    assert digit_or_special_present("ciao1") == True

def test_digit_or_special_present_punctuation():
    """
    Test the digit_or_special_present function
    GIVEN: a string containing punctuation
    WHEN: the function is called with this string
    THEN: the function returns True
    """
    assert digit_or_special_present("ciao!") == True

def test_digit_or_special_present_empty():
    """
    Test the digit_or_special_present function
    GIVEN: an empty string
    WHEN: the function is called with this string
    THEN: the function returns False
    """
    assert digit_or_special_present("") == False

def test_digit_or_special_present_spaces():
    """
    Test the digit_or_special_present function
    GIVEN: a string containing only spaces
    WHEN: the function is called with this string
    THEN: the function returns False
    """
    assert digit_or_special_present(" ") == False


def test_is_empty_or_only_space_nonEmpty():
    """
    Test the is_empty_or_only_space function
    GIVEN: a non-empty string with characters other than spaces
    WHEN: the function is called with this string
    THEN: the function returns False
    """
    assert is_empty_or_only_space("ciao ") == False

def test_is_empty_or_only_space_empty():
    """
    Test the is_empty_or_only_space function
    GIVEN: an empty string
    WHEN: the function is called with this string
    THEN: the function returns True
    """
    assert is_empty_or_only_space("") == True

def test_is_empty_or_only_space_onlySpaces():
    """
    Test the is_empty_or_only_space function
    GIVEN: a string containing only spaces
    WHEN: the function is called with this string
    THEN: the function returns True
    """
    assert is_empty_or_only_space(" ") == True

def test_is_vowel_lowVowel():
    """
    Test the is_vowel function.
    GIVEN: a lower ASCII vowel
    WHEN: the function is called with that char
    THEN: the function returns true
    """
    
    assert is_vowel('a') == True

def test_is_vowel_capitalVowel():
    """
    Test the is_vowel function.
    GIVEN: a capital ASCII vowel
    WHEN: the function is called with that vowel
    THEN: the function returns true
    """

    assert is_vowel('A') == True

def test_is_vowel():
    """
    Test the is_vowel function.
    GIVEN: a consonant
    WHEN: the function is called with a consonant
    THEN: the function returns false
    """
    assert is_vowel('b') == False


def test_divide_vowels_consonants_string():
    """
    Test the divide_vowels_consonants function
    GIVEN: an alphabetic string
    WHEN: the function is called with that string
    THEN: the function returns a tuple where the first element is vowel and the second consonants
    """
    result = divide_vowels_consonants("ciao")
    assert result[0] == "iao"
    assert result[1] == "c"

def test_divide_vowels_consonants_empty():
    """
    Test the divide_vowels_consonants function
    GIVEN: an empty string
    WHEN: the function is called with an empty string
    THEN: the function returns a tuple where both elements are empty strings
    """
    result = divide_vowels_consonants("")
    assert result[0] == ""
    assert result[1] == ""

def test_divide_vowels_consonants_spaces():
    """
    Test the divide_vowels_consonants function
    GIVEN: a string with spaces '  '
    WHEN: the function is called with '  '
    THEN: the function returns a tuple where both elements are empty strings
    """
    result = divide_vowels_consonants("  ")
    assert result[0] == ""
    assert result[1] == ""

def test_divide_vowels_consonants_singleVowel():
    """
    Test the divide_vowels_consonants function
    GIVEN: a vowel
    WHEN: the function is called with a vowel
    THEN: the function returns a tuple where the first element is that vowel and the second element is an empty string
    """
    result = divide_vowels_consonants("a")
    assert result[0] == "a"
    assert result[1] == ""

def test_divide_vowels_consonants_singleConsonant():
    """
    Test the divide_vowels_consonants function
    GIVEN: a consonant
    WHEN: the function is called with a consonant
    THEN: the function returns a tuple where the first element is an empty string and the second the consonant
    """
    result = divide_vowels_consonants("l")
    assert result[0] == ""
    assert result[1] == "l"




def test_is_name_ok_valid():
    """
    Test the is_name_ok function.
    GIVEN: a valid  name
    WHEN: the function is called with valid name
    THEN: the function returns true
    """
    assert  is_name_ok('cate')==True

def test_is_name_ok_digit():
    """
    Test the is_name_ok function.
    GIVEN: a string with digit
    WHEN: the function is called with that string
    THEN: the function returns false
    """
    
    assert  is_name_ok('cate5')==False

def test_is_name_ok_empty():
    """
    Test the is_name_ok function.
    GIVEN: an empty string
    WHEN: the function is called with an empty string
    THEN: the function returns false
    """
    assert  is_name_ok('')==False



def test_is_name_ok_punctation():
    """
    Test the is_name_ok function.
    GIVEN: a string with punctation
    WHEN: the function is called with that string
    THEN: the function returns false
    """
    assert  is_name_ok('gianmar.ia')==False #because i don't know where to divide it

def test_is_name_ok_spaces():
    """
    Test the is_name_ok function.
    GIVEN: a string representing a name with spaces
    WHEN: the function is called with that string
    THEN: the function returns true
    """
    assert  is_name_ok('gian maria')==True


def test_is_name_ok_nonAscii():
    """
    Test the is_name_ok function.
    GIVEN: a string with non ASCII character
    WHEN: the function is called with that string
    THEN: the function returns false
    """
    assert  is_name_ok('gianmarià')==False #name with accent

def test_is_surname_ok_valid():
    """
    Test the is_surname_ok function.
    GIVEN: a string representing a valid surname
    WHEN: the function is called with a valid surname
    THEN: the function returns true 
    """
    assert  is_surname_ok('cate')==True


def test_is_surname_ok_digit():
    """
    Test the is_surname_ok function.
    GIVEN: a string with digit
    WHEN: the function is called that string
    THEN: the function returns false
    """
    assert  is_surname_ok('cate5')==False


def test_is_surname_ok_empty():
    """
    Test the is_surname_ok function.
    GIVEN: an empty string
    WHEN: the function is called with an empty string
    THEN: the function returns true
    """
    assert  is_surname_ok('')==True
 
  

def test_is_surname_ok_punctation():
    """
    Test the is_surname_ok function.
    GIVEN: a string containing punctation
    WHEN: the function is called with that string
    THEN: the function returns false
    """
    assert  is_surname_ok('bianchi.rossi')==False

def test_is_surname_ok_spaces():
    """
    Test the is_surname_ok function.
    GIVEN: a valid string with spaces
    WHEN: the function is called with that string
    THEN: the function returns true
    """
    assert  is_surname_ok('bianchi rossi')==True
    assert  is_surname_ok(' bianchi rossi')==True

def test_is_surname_ok_nonAscii():
    """
    Test the is_surname_ok function.
    GIVEN: a string containing non ASCII char
    WHEN: the function is called with that string
    THEN: the function returns false
    """
    assert  is_surname_ok('bianchi rossè ')==False #non ASCII


def test_is_gender_ok_valid_male():
    """
    Test the is_gender_ok function.
    GIVEN: a valid string representing a male
    WHEN: the function is called with valid male string
    THEN: the function returns true
    """
    assert is_gender_ok('m') == True

def test_is_gender_ok_valid_spaces():
    """
    Test the is_gender_ok function.
    GIVEN: a valid string representing a male with spaces
    WHEN: the function is called with valid male string with spaces
    THEN: the function returns true
    """
    assert is_gender_ok('M   ') == True
    

def test_is_gender_ok_valid_female():
    """
    Test the is_gender_ok function.
    GIVEN: a valid string representing a female
    WHEN: the function is called with a valid female char
    THEN: the function returns true
    """
    assert is_gender_ok('F') == True


def test_is_gender_ok_invalid():
    """
    Test the is_gender_ok function.
    GIVEN: an invalid string (not M m F f)
    WHEN: the function is called with an invalid string
    THEN: the function returns false
    """
    assert is_gender_ok('maschio') == False

def test_is_place_of_birth_ok_valid():
    """
    Test the is_place_of_birth_ok function.
    GIVEN: a string representing a valid place of birth
    WHEN: the function is called with a valid place
    THEN: the function returns true
    """
    assert is_place_of_birth_ok('Roma') == True

def test_is_place_of_birth_ok_digit():
    """
    Test the is_place_of_birth_ok function.
    GIVEN: a string representing a place of birth with digit
    WHEN: the function is called with a string with digit
    THEN: the function returns false
    """
   
    assert is_place_of_birth_ok('Roma2') == False


def test_is_place_of_birth_ok_empty():
    """
    Test the is_place_of_birth_ok function.
    GIVEN: an empty string
    WHEN: the function is called with an empty string
    THEN: the function returns false
    """

    assert is_place_of_birth_ok('') == False


def test_is_place_of_birth_ok_spaces():
    """
    Test the is_place_of_birth_ok function.
    GIVEN: a string with only spaces
    WHEN: the function is called with a spaces string
    THEN: the function returns false
    """
    assert is_place_of_birth_ok('   ') == False


def test_gender_to_boolean_male():
    """
    Test the gender_to_boolean function.
    GIVEN: a char representing a male
    WHEN: the function is called with a male char
    THEN: the function returns true if the string is M or m
    """
    assert gender_to_boolean('M') == True
    assert gender_to_boolean('m') == True


def test_gender_to_boolean_female():
    """
    Test the gender_to_boolean function.
    GIVEN: a char representing a gender
    WHEN: the function is called with a gender char
    THEN: the function returns false if the string is F or f
    """
    assert gender_to_boolean('F') == False
    assert gender_to_boolean('f') == False



def test_last_two_digits_fourdigit():
    """
    Test the last_two_digits function.
    GIVEN: an integer number with four digit
    WHEN: the function is called with that number
    THEN: the function returns the last two digits of the number
    """
    assert last_two_digits(2023) == '23'


def test_last_two_digits_onedigit():
    """
    Test the last_two_digits function.
    GIVEN: an integer number with one digit
    WHEN: the function is called with that number
    THEN: the function returns zero and that number
    """
    assert last_two_digits(5) == '05'

def test_last_two_digits_zero():
    """
    Test the last_two_digits function.
    GIVEN: an integer 0
    WHEN: the function is called with that number
    THEN: the function returns 00
    """
    assert last_two_digits(0) == '00'



def test_even_position_to_number_valid():
    """
    Test the even_position_to_number function
    
    GIVEN: A valid ASCII upper char or a digit
    WHEN: the function is called with that number or char
    THEN: the function return a number acoording to Agenzia Entrate
    roules
    """
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