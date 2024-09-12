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

    # Check each character in the string
    for char in input_string:
        # If the character is a digit or a special character, return True
        if char.isdigit() or char in special_characters:
            return True

    # If no digits or special characters are found, return False
    return False
