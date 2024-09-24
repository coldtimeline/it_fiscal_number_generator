import argparse
import configparser

import pandas as pd
from datetime import datetime
from src.ask_functions import get_name, get_surname, get_gender, get_date_of_birth, get_dataframe_from_html
from src.ask_functions import get_place_of_birth
from src.generate_functions import generate_fiscal_code

def run_program_from_cl():
    """
    Runs the program from the command line, prompting the user for personal information
    and generating a fiscal code based on the provided data.

    The function performs the following steps:
    1. Prompts the user to input their name, surname, gender, date of birth, and place of birth.
    2. Retrieves a dataset of place codes from an HTML file.
    3. Generates and prints the fiscal code based on the provided information and dataset.

    It catches and prints any exceptions that occur during the execution of the function.
    """

    try:
      name = get_name()
      surname = get_surname()
      gender = get_gender()
      date_of_birth = get_date_of_birth()      
      place_dataset = get_dataframe_from_html('codici_comuni.htm')
      place = get_place_of_birth(place_dataset)

      print("your fiscal code is:")
      print(generate_fiscal_code(name,surname,gender,date_of_birth,place,place_dataset))
    except Exception as e:
      print(e)

def run_program_from_ini_file(file_path):
    """
    Runs the program using configuration from an INI file, 
    and generating a fiscal code based on the provided data.

    This function performs the following steps:
    1. Reads the configuration from the specified INI file.
    2. Retrieves personal information from the INI file.
    3. Retrieves a dataset of place codes from an HTML file.
    4. Generates and prints the fiscal code based on the provided information and dataset.
    It catches and prints any exceptions that occur during the execution of the function.

    Args:
        file_path (str): The path to the INI file containing the configuration.
    """ 
    try:
      config = configparser.ConfigParser()
      config.read(file_path)

      name = get_name(True,config.get('PERSON', 'name'))
      surname = get_surname(True,config.get('PERSON', 'surname'))
      gender = get_gender(True,config.get('PERSON', 'gender'))
      date_of_birth = get_date_of_birth(True,config.get('PERSON', 'date_of_birth'))      
      place_dataset = get_dataframe_from_html('codici_comuni.htm')
      place = get_place_of_birth(place_dataset,True,config.get('PERSON', 'place_of_birth'))

      print("your fiscal code is:")
      print(generate_fiscal_code(name,surname,gender,date_of_birth,place,place_dataset))
    except Exception as e:
      print(e)
   
   

def main():
    
    parser = argparse.ArgumentParser(description="Read user data from config or input")
    parser.add_argument('--config', type=str, help='Path to the config file')
    args = parser.parse_args()

    
    if args.config:
        run_program_from_ini_file(args.config)
    else:
        run_program_from_cl()


if __name__ == "__main__":
    main()





