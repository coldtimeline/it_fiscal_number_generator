import sys
import os

#add path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))



from src.generate_functions import generate_day_gender_code

def test_generate_day_gender_code():
    """
    Test the generate_day_gender_code function.
    GIVEN: a bool representing Male (true) or Female (false) and an int representing a day of birth
    WHEN: the function is called with a gender bool and the day of birth
    THEN: the function returns the day of birth if the gender is male, otherwise the day of birth plus 40
    """

    assert generate_day_gender_code(True, 15) == 15  # Male, should return the day of birth
    assert generate_day_gender_code(False, 15) == 55  # Female, should return the day of birth plus 40
