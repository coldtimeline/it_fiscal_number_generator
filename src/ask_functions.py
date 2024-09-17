import sys
import os
import pandas as pd
from datetime import datetime


#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.support_functions import is_name_ok, is_surname_ok, is_gender_ok, is_gender_ok, is_place_of_birth_ok
from src.support_functions import select_string, find_similar_strings

def get_dataframe_from_webpage(path_to_page):
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



def get_name():
    """
    Asks the user for their name and checks if it is valid using
    the is_name_ok function.

    Returns:
    str: The valid name entered by the user.

    Raises:
    ValueError if the name is not valid.
    """
    name = input("Please enter your name (ascii format), no digit or punctation allowed: ")
    if not is_name_ok(name):
        raise ValueError("The name entered is not valid. No digit or punctation allowed")
    return name


def get_surname():
    """
    Asks the user for their surname and checks if it is valid using
    the is_surname_ok function.

    Returns:
    str: The valid surname entered by the user.

    Raises:
    ValueError if the surname is not valid.
    """
    surname = input("Please enter your surname (ASCII format), no digit or punctation allowed: ")
    if not is_surname_ok(surname):
        raise ValueError("The surname entered is not valid. No digit or punctation allowed")
    return surname

def get_gender():
    """
    Asks the user for their gender and checks if it is valid using the is_gender_ok function.
    Raises a ValueError if the gender is not valid.

    Returns:
    str: The valid gender entered by the user.

    Raises:
    ValueError if the gender is not valid.
    """
    gender = input("Please enter your gender (M/F): ")
    if not is_gender_ok(gender):
      raise ValueError("The gender entered is not valid. Please enter only one m or f")

    return gender





def get_date_of_birth():
    """
    This function prompts the user for their date of birth.
    The date of birth should be entered in the format: DD-MM-YYYY.

    Returns:
    datetime: A datetime object representing the user's date of birth.
    """
    # Prompt the user for their date of birth
    date_of_birth_str = input("Please enter your date of birth (DD-MM-YYYY): ")

    # Convert the string to a datetime object
    # If the date is not in the correct format, this function will raise a ValueError
    date_of_birth = datetime.strptime(date_of_birth_str, "%d-%m-%Y")

    return date_of_birth



def get_place_of_birth(df):
    """
    This function prompts the user for their place of birth.
    Then searches for the place in the dataset and returns the right name of the
    place

    Parameters:
    df (DataFrame): The dataframe containing the place codes

    Returns:
    str: The name of the place of birth.

    Raises: 
    ValueError if the place of birth contains digit or is empty
    """
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

