import sys
import os
import pandas as pd
from datetime import datetime


#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.support_functions import is_name_ok, is_surname_ok, is_gender_ok, is_gender_ok, is_place_of_birth_ok
from src.support_functions import select_string, find_similar_strings

def get_dataframe_from_html(path_to_page):
    """
    This function takes a path or an URL of a webpage containing an HTML table and returns a pandas DataFrame.
    In particular, the firts table of the webpage is returned.

    Parameters:
    path_to_page (str): The URL or path of the webpage containing the HTML table.

    Returns:
    df (DataFrame): A pandas DataFrame containing the data from the HTML table.

    Raises:
    ValueError: If the path or URL does not contain a valid HTML table, or if other error occurs during the reading process.
    """
    try:
        # Use the pandas read_html function to read the HTML table into a list of DataFrames
        dfs = pd.read_html(path_to_page)

        # Check if any tables were found
        if not dfs:
            raise ValueError("No tables found at the provided path")

        # Return the first table found
        return dfs[0]

    except Exception as e:
        # If an error occurs, raise it
        raise ValueError(f"An error occurred while trying to read the HTML table: {e}")



def get_name(from_ini=False,name=""):
    """
    This function:
    - if parameter from_ini is True, checks if the parameter name is a valid name
    - if parameter from_ini is False, ask the user its name and checks if it is valid

    Parameters:
    from_ini (bool, Optional): represent if the function is called with data from a config file (True) or not (False)
    name (string, Optional): the name that has been read from a config file

    Returns:
    str: The valid name entered from config file or by the user.

    Raises:
    ValueError if the name is not valid.
    """

    if from_ini:
        if not is_name_ok(name):
            raise ValueError("The name entered is not valid. No digit or punctation allowed")
    else:
        name = input("Please enter your name (ascii format), no digit or punctation allowed: ")
        if not is_name_ok(name):
            raise ValueError("The name entered is not valid. No digit or punctation allowed")
    
    return name


def get_surname(from_ini=False, surname=""):
    """
    This function:
    - if parameter from_ini is True, checks if the parameter surname is a valid surname
    - if parameter from_ini is False, ask the user its surname and checks if it is valid

    Parameters:
    from_ini (bool, Optional): represent if the function is called with data from a config file (True) or not (False)
    surname (string, Optional): the surname that has been read from a config file

    Returns:
    str: The valid surname entered from config file or by the user.

    Raises:
    ValueError if the surname is not valid.
    """
    if from_ini:
        if not is_surname_ok(surname):
            raise ValueError("The surname entered is not valid. No digit or punctation allowed")
    else:
        surname = input("Please enter your surname (ASCII format), no digit or punctation allowed: ")
        if not is_surname_ok(surname):
            raise ValueError("The surname entered is not valid. No digit or punctation allowed")
    return surname

def get_gender(from_ini=False, gender=""):
    """
    This function:
    - if parameter from_ini is True, checks if the parameter gender is a valid gender
    - if parameter from_ini is False, ask the user its gender and checks if it is valid

    Parameters:
    from_ini (bool, Optional): represent if the function is called with data from a config file (True) or not (False)
    gender (string, Optional): the gender that has been read from a config file

    Returns:
    str: The valid gender entered from config file or by the user.

    Raises:
    ValueError if the gender is not valid.
    """
    if from_ini:
        if not is_gender_ok(gender):
            raise ValueError("The gender entered is not valid. Please enter only one m or f")
    else:
        gender = input("Please enter your gender (M/F): ")
        if not is_gender_ok(gender):
            raise ValueError("The gender entered is not valid. Please enter only one m or f")

    return gender





def get_date_of_birth(from_ini=False, date_of_birth_str=""):
    """
    This function:
    - if parameter from_ini is True, transform the parameter date_of_birth_str in a datetime object
    - if parameter from_ini is False, ask the user its date of birth and transforms
      it in a datetime object
    
    Parameters:
    from_ini (bool, Optional): represent if the function is called with data from a config file (True) or not (False)
    date_of_birth_str (string, Optional): represent the date of birth that has been read from config file
    
    Returns:
    datetime: A datetime object representing the user's date of birth.

    Raises:
    ValueError: datetime.strptime function raises error if the date is not in the
    correct format
    """

    if from_ini:
        # If the date is not in the correct format, this function will raise a ValueError
        date_of_birth = datetime.strptime(date_of_birth_str, "%d-%m-%Y")
    else:  
        # Prompt the user for their date of birth
        # and Convert the string to a datetime object
        # If the date is not in the correct format, this function will raise a ValueError
        date_of_birth_str = input("Please enter your date of birth (DD-MM-YYYY): ")
        date_of_birth = datetime.strptime(date_of_birth_str, "%d-%m-%Y")

    return date_of_birth



def get_place_of_birth(df, from_ini=False, place_of_birth=""):
    """
    This function:
    - if parameter from_ini is True, checks if place_of_birth is valid
    - if parameter from_ini is False, ask the user its place of birth and checks if is valid
    Then searches for the place in the dataset and returns the right name of the
    place

    Parameters:
    df (DataFrame): The dataframe containing the place codes
    from_ini (bool, Optional): represent if the function is called with data from a config file (True) or not (False) 
    place_of_birth (string, Optional): the place of birth that has been read from config file

    Returns:
    str: The name of the place of birth.

    Raises: 
    ValueError if the place of birth contains digit or is empty
    """
    if from_ini:
        if not is_place_of_birth_ok(place_of_birth):
            raise ValueError("The place of birth entered is not valid. No digit or empty string allowed")
    else:
        place_of_birth = input("Please enter your city (comune) of birth: ")
        if not is_place_of_birth_ok(place_of_birth):
            raise ValueError("The place of birth entered is not valid. No digit or empty string allowed")

    #string to capital letter because string are in capital letter in dataframe we used
    place_of_birth = place_of_birth.upper()
    
    #to find the correct place of birth:
    #find_similar_string search for city with similar names in the dataset
    #select_string select which one of the found string is the right one
    place_of_birth_found = select_string(find_similar_strings(df, 'DESCRIZIONE COMUNE', place_of_birth))

    return place_of_birth_found

