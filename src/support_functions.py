import string

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