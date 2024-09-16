import pandas as pd
from datetime import datetime
from src.ask_functions import get_name, get_surname, get_gender, get_date_of_birth, get_dataframe_from_web
from src.ask_functions import get_place_of_birth
from src.generate_functions import generate_fiscal_code

def run_program():
    try:
      name = get_name()
      surname = get_surname()
      gender = get_gender()
      date_of_birth = get_date_of_birth()

      #place_dataset = get_dataframe_from_web('https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php')
      place_dataset = get_dataframe_from_web('codici_comuni.htm')
      place = get_place_of_birth(place_dataset)

      print("your fiscal code is:")
      print(generate_fiscal_code(name,surname,gender,date_of_birth,place,place_dataset))
    except Exception as e:
      print(e)

run_program()