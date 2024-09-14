import string

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