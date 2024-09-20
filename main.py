import argparse
import configparser

import pandas as pd
from datetime import datetime
from src.ask_functions import get_name, get_surname, get_gender, get_date_of_birth, get_dataframe_from_html
from src.ask_functions import get_place_of_birth
from src.generate_functions import generate_fiscal_code

def run_program_from_cl():
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





