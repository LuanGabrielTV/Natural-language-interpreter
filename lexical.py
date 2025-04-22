from alphabet import allowed_characters
from paths import input_path
from errors import *
from stop_words import stop_words_list

def read_file():
    global input_string

    with open(input_path, 'r') as file:
        input_string = file.read()


def check_alphabet():
    global input_string
    valid = all(character in allowed_characters for character in input_string)

    if valid == False:
        invalid = [character for character in input_string if character not in allowed_characters]
        if len(invalid)>1:
            print(invalid_alphabet_error.format('s', 's', ','.join(invalid), 'são', 's'))
        else:
            print(invalid_alphabet_error.format('', '', ','.join(invalid), 'é', ''))
        exit(1)
        

if __name__ == '__main__':
   read_file()
   check_alphabet()
   