import sys
import os
import string
import pandas as pd

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.support_functions import odd_position_to_number,even_position_to_number

def generate_day_gender_code(gender, day_of_birth):
    """
    Determine the day of birth part of the code based on gender.

    Parameters:
    gender (bool): The gender of the individual, where True represents male and False represents female.
    day_of_birth (int): The day of birth of the individual.

    Returns:
    int: The original day of birth if the gender is male, otherwise the day of birth plus 40.
    """
    # Check if the input gender is True (male) return return the day of birth as
    # it is, otherwise add 40
    if gender:
        return day_of_birth
    else:
        return day_of_birth + 40


def generate_name_code(vowels_ucase, consonants_ucase):
    """
    Generates a three-character string based on the consonants and vowels
    of the name, according to agenzia delle entrate rules.

    Parameters:
    vowels_ucase (str): String containing all the vowels of the name, unknown case.
    consonants_ucase (str): String containing all the consonants of the name, unknown case.

    Returns:
    str: A three-character string according to the specified rules.

    Raises:
    ValueError: If the input name is invalid (empty)
    """

    # Initialize the output string
    code = ""
    # Make consonants and vowels upper case
    consonants = consonants_ucase.upper()
    vowels = vowels_ucase.upper()
    #eliminate all spaces that may be present
    consonants = consonants.replace(" ", "")
    vowels = vowels.replace(" ", "")

    # Case 1: Four or more consonants
    if len(consonants) >= 4:
        code = consonants[0] + consonants[2] + consonants[3]
    # Case 2: Three consonants
    elif len(consonants) == 3:
        code = consonants[0] + consonants[1] + consonants[2]
    # Case 3: Two consonants and one vowels
    elif len(consonants) == 2 and len(vowels) >= 1:
        code = consonants[0] + consonants[1] + vowels[0]
    # Case 4: Two consonants and no vowels
    elif len(consonants) == 2 and len(vowels) == 0:
        code = consonants[0] + consonants[1] + 'X'
    # Case 5: One consonants and two vowels
    elif len(consonants) == 1 and len(vowels) >= 2:
        code = consonants[0] + vowels[0] + vowels[1]
    # Case 6: One consonants and one vowel
    elif len(consonants) == 1 and len(vowels) == 1:
        code = consonants[0] + vowels[0] + 'X'
    # Case 7: One consonants and zero vowel
    elif len(consonants) == 1 and len(vowels) == 0:
        code = consonants[0] + 'X' + 'X'
    # Case 8: Zero consonants and three vowel
    elif len(consonants) == 0 and len(vowels) >= 3:
        code = vowels[0] + vowels[1] + vowels[2]
    # Case 9: Zero consonants and two vowel
    elif len(consonants) == 0 and len(vowels) == 2:
        code = vowels[0] + vowels[1] + 'X'
    # Case 10: Zero consonants and one vowel
    elif len(consonants) == 0 and len(vowels) == 1:
        code = vowels[0] + 'X' + 'X'

    # Case 11: Zero consonants and zero vowel is not permitted, so rise an error
    else:
        raise ValueError("Invalid input name")

    return code


def generate_surname_code(vowels_ucase, consonants_ucase):
    """
    Generates a three-character string based on the consonants and vowels
    of the surname, according to agenzia delle entrate rules.

    Parameters:
    vowels_ucase (str): String containing all the vowels of the name, unknown case.
    consonants_ucase (str): String containing all the consonants of the name, unknown case.

    Returns:
    str: A three-character string according to the specified rules.
    """
    
    code = ""
    # Make consonants and vowels upper case
    consonants = consonants_ucase.upper()
    vowels = vowels_ucase.upper()
    #eliminate all spaces that may be present
    consonants = consonants.replace(" ", "")
    vowels = vowels.replace(" ", "")



    # Case 1: Four or more consonants
    if len(consonants) >= 3:
        code = consonants[0] + consonants[1] + consonants[2]
    # Case 1: Two consonants and one vowels
    elif len(consonants) == 2 and len(vowels) >= 1:
        code = consonants[0] + consonants[1] + vowels[0]
    # Case 2: Two consonants and no vowels
    elif len(consonants) == 2 and len(vowels) == 0:
        code = consonants[0] + consonants[1] + 'X'
    # Case 3: One consonants and two vowels
    elif len(consonants) == 1 and len(vowels) >= 2:
        code = consonants[0] + vowels[0] + vowels[1]
    # Case 4: One consonants and one vowel
    elif len(consonants) == 1 and len(vowels) == 1:
        code = consonants[0] + vowels[0] + 'X'
    # Case 5: One consonants and zero vowel
    elif len(consonants) == 1 and len(vowels) == 0:
        code = consonants[0] + 'X' + 'X'
    # Case 6: Zero consonants and three vowel
    elif len(consonants) == 0 and len(vowels) >= 3:
        code = vowels[0] + vowels[1] + vowels[2]
    # Case 7: Zero consonants and two vowel
    elif len(consonants) == 0 and len(vowels) == 2:
        code = vowels[0] + vowels[1] + 'X'
    # Case 8: Zero consonants and one vowel
    elif len(consonants) == 0 and len(vowels) == 1:
        code = vowels[0] + 'X' + 'X'
    # Case 9: Zero consonants and zero vowel
    else:
        code = 'XXX'


    return code

def generate_month_char(month):
    """
    Converts an integer number (representing month of birth)
    to a corresponding character based on Agenzia delle Entrate rules

    Parameters:
    month (int): The input integer number representing the month.

    Returns:
    str: The corresponding character as per the rules.

    Raises:
    ValueError: If the number is not between 1 and 12 inclusive.
    """
    # Dictionary mapping numbers to characters
    number_char_map = {
        1: 'A', 5: 'E', 9: 'P',
        2: 'B', 6: 'H', 10: 'R',
        3: 'C', 7: 'L', 11: 'S',
        4: 'D', 8: 'M', 12: 'T'
    }

    # Check if the number is in the valid range
    if month not in number_char_map:
        raise ValueError("Month must be between 1 and 12 inclusive.")

    # Return the corresponding character
    return number_char_map[month]

def generate_last_characther(input_code):
    """
    This function take the string of uncompleted code and return the last character
    that must be added to the code to complete it, based on rules
    from Agenzia dell'Entrate

    Parameters:
    input_code (str): the string of uncompleted code

    Returns:
    char: the new last character of the code

    Raises:
    ValueError: If the input code length is different from 15 characters
    """

    if input_code == "":
        raise ValueError("Input code cannot be empty")
    if len(input_code) != 15:
        raise ValueError("Input code must have 15 characters")

   
    input_code_even = ""
    input_code_odd = ""
    odd_position_sum=0
    even_position_sum=0


    # Dividing the string in odd and even position, using string slicing
    # Agenzia delle entrate consider the first character as in a odd position
    input_code_even = input_code[1::2]
    input_code_odd = input_code[::2]


    for char in input_code_odd:
        odd_position_sum += odd_position_to_number(char)

    for char in input_code_even:
        even_position_sum += even_position_to_number(char)


    total_sum = odd_position_sum + even_position_sum
    last_digit_number = total_sum % 26
    last_digit_char = chr(last_digit_number + 65)

    return last_digit_char

def generate_city_code(city_df, city_name):
    """
    This function searches for a city in the 'DESCRIZIONE COMUNE' column of the dataframe
    and returns its corresponding code from the 'CODICE BELFIORE' column.

    Parameters:
    city_df (pandas.DataFrame): The dataframe containing the city data.
    city_name (str): The name of the city to search for.

    Returns:
    str: The code of the city if found, otherwise None.

    Raises:
    ValueError: If the city is not found in the dataframe.
    """

    #access the first dataframe
    #city_df = city_df[0]

    # Filter the dataframe to find the row with the given city name
    city_row = city_df[city_df['DESCRIZIONE COMUNE'] == city_name]

    # Check if the city was found and return the corresponding code
    if not city_row.empty:
        return city_row['CODICE BELFIORE'].values[0]
    else:
        raise ValueError("city row not found")