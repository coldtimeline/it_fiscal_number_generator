import string
from fuzzywuzzy import fuzz
import pandas as pd

def digit_or_special_present(input_string):
    """
    Check if the input string contains any numbers or special characters.

    Parameters:
    input_string (str): The string to be checked.

    Returns:
    bool: True if the string contains numbers or special characters, False otherwise.
    """

    # Define the set of special characters
    special_characters = set(string.punctuation)

    for char in input_string:
        # If the character is a digit or a special character, return True
        if char.isdigit() or char in special_characters:
            return True

    # If no digits or special characters are found, return False
    return False


def is_empty_or_only_space(s):
    """
    This function checks if a given string is not empty or only spaces.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is empty or only spaces, False otherwise.
    """

    # If the string is empty or only spaces, return True
    if s.strip() == '':
        return True

    # If the string is not empty and not only spaces, return False
    return False


def is_vowel(char):
    """
    Check if the provided character is a vowel.

    Parameters:
    char (str): A single character to be checked.

    Returns:
    bool: True if the character is a vowel, False otherwise.
    """

    # Define a list of vowels: accented not inserted 
    #because they are not ASCII character
    vowels = 'aeiouAEIOU' 

    # Check if the character is a vowel
    return char in vowels


def divide_vowels_consonants(word):
    """
    This function takes a word as input and returns two string:
    one containing the vowels and the other containing consonants.
    This function works only with alphabetic characters, so the imput word should be
    controlled before calling this function.

    Parameters:
    word (str): The input word.

    Returns:
    vowels (str): The string containing the vowels.
    consonants (str): The string containing the consonants.
    """


    # Initialize empty strings for vowels and consonants
    vowels = ""
    consonants = ""
    # Eliminate al spaces that may be present
    word_wo_spaces = word.replace(" ", "")

    # Iterate through each character in the word, checking if is a vowel or not
    for char in word_wo_spaces:
        if is_vowel(char):
            vowels += char
        else:
            consonants += char

    return vowels, consonants


def is_name_ok(name):
    """
    This function checks if a given name is valid. The name is valid if it is
    not empty or not contains only spaces and does not contain any
    special characters or numbers. Name should be also written in ASCII

    Parameters:
    name (str): The name to check.

    Returns:
    bool: True if the name is valid, False otherwise.
    """

    # Check if the name is not empty or only spaces
    if is_empty_or_only_space(name):
        return False

    # Check if the name contains only letters. Not use the isalpha() string
    # method because it does not work with spaces that may be present in
    # the name. Points or similar are not accepted as separator
    if digit_or_special_present(name):
        return False

    # Check if contains non ascii character, no accented letter or diacritical accepted
    if not name.isascii():
        return False

    # If the name is valid, return True
    return True


def is_surname_ok(surname):
    """
    This function checks if a given surname is valid. The surname is valid if
    it is empty or contains only spaces or does not contain any
    special characters or numbers.
    Parameters:
    surname (str): The surname to check.

    Returns:
    bool: True if the surname is valid, False otherwise.

    """
    # Check if the surname contains only letters. Not use the isalpha() string
    # method because it does not work with spaces that may be present in
    # the surname
    if digit_or_special_present(surname):
        return False
    # Check if contains non ascii character, no accented letter or diacritical accepted
    if not surname.isascii():
        return False

    return True

def is_gender_ok(gender):
    """
    This function checks if the gender is M or F. In particular M,m,F,f are
    allowed, or those letter with spaces.

    Parameters:
    gender (str): The gender to check.

    Returns:
    bool: True if the gender is valid, False otherwise.
    """

    if gender.strip() == 'M' or gender.strip() == 'm' or gender.strip() == 'F' or gender.strip() == 'f':
       return True
    else:
       return False
    
def is_place_of_birth_ok(place_of_birth):
    """
    This function checks if the place of birth is valid. In particular should not
    be empty or only spaces, and digit should not be present.
    Doesn't check for ASCII because some accented letter may be present.
  
    Parameters:
    place_of_birth (str): The place of birth to check.
  
    Returns:
    bool: True if the place of birth is valid, False otherwise.
    """
  
    # Check if the place of birth is not empty or only spaces
    if is_empty_or_only_space(place_of_birth):
      return False
  
    #Check if nubers are present, cannot use isdigit() on the string because if
    #place of birth contains digit and characters, isdigit() return false
    for char in place_of_birth:
      if char.isdigit():
        return False
  
    return True

def gender_to_boolean(gender):
    """
    This function takes a string representing the gender and returns a boolean
    value. If the gender is 'M' or 'm' return true, if the gender is 'F' or 'f'
    return false. Should be called only if the gender is valid.
  
    Parameters:
    gender (str): The input gender.
  
    Returns:
    bool: The corresponding boolean value 
    """
    if gender.strip() == 'M' or gender.strip() == 'm':
      return True
    else:
      return False

def last_two_digits(number):
    """
    This function takes a number as input and returns the last two digits of that number.
    doesn't check if the number is negative because datetime month, year and day can only
    be positive and integer number

    Parameters:
    number (int): representing year or day of birth

    Returns:
    str: The last two digits of the year or day as a two-digit string
    """

    number_str = str(number)

    # Get the last two digits
    last_two_digits = number_str[-2:]

    # If the year has less than two digits, prepend a '0',
    if len(last_two_digits) < 2:
        last_two_digits = '0' + last_two_digits

    return last_two_digits


def even_position_to_number(char):
    """
    This function take a char which must be an upper character or a digit and
    returns a value according to agenzia delle entrate rules, for even positioned
    characters or digits

    Parameters:
    char (char): the char to convert

    Returns:
    int: the converted value

    Raises:
    ValueError: If the input character is not present.
    """

    # Dictionary mapping numbers to characters
    even_position_to_number_map = {
        "A": 0, "0": 0,
        "B": 1, "1": 1,
        "C": 2, "2": 2,
        "D": 3, "3": 3,
        "E": 4, "4": 4,
        "F": 5, "5": 5,
        "G": 6, "6": 6,
        "H": 7, "7": 7,
        "I": 8, "8": 8,
        "J": 9, "9": 9,
        "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19,
        "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25

    }

    # Check if the character is in the map
    if char not in even_position_to_number_map:
        raise ValueError("Invalid character present")

    # Return the corresponding value
    return even_position_to_number_map[char]

def odd_position_to_number(char):
    """
    This function take a char which must be an upper character or a digit and
    returns a value according to agenzia delle entrate rules, for odd positioned
    characters or digits

    Parameters:
    char (char): the char to convert

    Returns:
    int: the converted value

    Raises:
    ValueError: If the input character is not present.
    """

    # Dictionary mapping numbers to characters
    odd_position_to_number_map = {
        "A": 1, "0": 1,
        "B": 0, "1": 0,
        "C": 5, "2": 5,
        "D": 7, "3": 7,
        "E": 9, "4": 9,
        "F": 13, "5": 13,
        "G": 15, "6": 15,
        "H": 17, "7": 17,
        "I": 19, "8": 19,
        "J": 21, "9": 21,
        "K":2, "L":4, "M":18, "N":20, "O":11, "P":3, "Q":6, "R":8, "S":12, "T":14,
        "U":16, "V":10, "W":22, "X":25, "Y":24, "Z":23

    }

    # Check if the character is in the map
    if char not in odd_position_to_number_map:
        raise ValueError("Invalid character")

    # Return the corresponding value
    return odd_position_to_number_map[char]



def find_similar_strings(df, column, input_string, threshold=80):
    """
    This function searches for strings similar to the input string in a specific column
    of a pandas DataFrame.

    Parameters:
    df (DataFrame): The pandas DataFrame to search.
    column (str): The column in the DataFrame to search.
    input_string (str): The string to find similar strings to.
    threshold (int): The similarity threshold. Strings with a similarity score above this 
    threshold will be considered similar.
    threshold 80 to get some similar string but not too much

    Returns:
    similar_strings (list): A list of strings found to be similar to the input string.

    Raises:
    ValueError: If no similar strings are found, or name of column have changed
    """
    # Ensure the column exists in the DataFrame, maybe name has changed
    if column not in df.columns:
        raise ValueError(f"The column '{column}' does not exist in the DataFrame.")

    # Find similar strings: create a list with a loop, string acceppted only if the test is true
    similar_strings = [str for str in df[column] if fuzz.ratio(input_string, str) > threshold]

    # Raise an error if no similar strings are found
    if not similar_strings:
        raise ValueError(f"No strings similar to '{input_string}' were found in the column '{column}'.")

    return similar_strings
