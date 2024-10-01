# it_fiscal_number_generator
This repository contains a python code that calculate italian fiscal code for people born in Italy

## Description
The fiscal code is a combination of 16 characther and digits and it is used to uniquely identify each person with the public administration. It is usually assigned at birth.

### How it is calculated
The fiscal code depends on:
1. Surname
2. Name
3. Date of birth
4. Gender
5. Place of birth

In fact, the first three character are a combination of letters of the surname, followed by three characters representing the name, then two digits representing the year of birth, a char representing the month of birth, two digits that simultaneusly represent the day of birth and the gender of a person, then four character representing the city (italian: comune) of birth and eventually a control character. You can find the roules in references.
## Installation

1. From terminal, go to the folder where you want to clone the repository and clone it:
    ```bash
    git clone https://github.com/coldtimeline/it_fiscal_number_generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd it_fiscal_number_generator
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the program:
    - you can simply run the program with data you'll enter from CL, using:
         ```bash
         python main.py
         ```
    - you can modify the person.ini file with your data and then run the program with that data:
         ```bash
         python main.py --config person.ini
         ```
        The data you write in the person.ini file should respect INPUT INFORMATION given below.
        You can also modify the name of the file and run the program with that file name.
## Usage

After you run the program, if no .ini file is given, it will ask to you your name, surname, gender, date and place of birth.
Then it return the string of your fiscal code. In this program the fiscal can be calculated only for people born in Italy.

### IMPORTANT INPUT INFORMATION
1. The name must be entered using only ASCII character, no punctation and digits are allowed.
2. The surname must be entered using only ASCII character, no punctation and digits are allowed. If you have no surname you can replace it with a space.
3. The letters accepted for the gender are only M or m for male and F or f for female
4. The date of birth must be entered with the format DD-MM-YYYY
5. The place of birth must be entered without digits. Must be an Italian city (italian: comune). To find your place of birth, the program finds the most similar places to the string you entered: for this reason it is better to enter the complete name of your birth city. To better know how to write your city name check references

### IMPORTANT OUTPUT INFORMATION

The only official italian fiscal code is the one given from Agenzia Delle Entrate, because there can be cases of different person with the same code (italian: omocodia), in particular for people with common name and surname and born in big cities. For this reason, be aware that the result of this program is a guess of what your code could be according to the data entered.

## References
This code was built following the roules presented in this page from [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/web/guest/schede/istanze/richiesta-ts_cf/informazioni-codificazione-pf), and the table for the place of birth was obtained saving this webpage [Elenco Codici comuni](https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php)