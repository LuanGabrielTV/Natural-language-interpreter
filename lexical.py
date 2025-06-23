from alphabet import allowed_characters, separators
from paths import input_path
from errors import *
from stop_words import stop_words_list
from queue import Queue
import re

def read_file():
    global input_string

    with open(input_path, 'r') as file:
        input_string = file.read()

def check_alphabet():
    global input_string
    valid = all(character in allowed_characters for character in input_string)

    if valid == False:
        invalid = [character for character in input_string if character not in allowed_characters]
        print(invalid)
        if len(invalid)>1:
            print(invalid_alphabet_error.format('s', 's', ','.join(invalid), 'são', 's'))
        else:
            print(invalid_alphabet_error.format('', '', ','.join(invalid), 'é', ''))
        
        return False

    return True
    
def generate_token_queue():
    global input_string, valid_words_list, stop_words_list, token_queue
    
    escaped_separators = '|'.join([re.escape(sep) for sep in separators])
    regex = r'(' + escaped_separators + ')'
    phrases_list = re.split(regex, input_string)
    words_list = []

    for phrase in phrases_list:
        words_list.extend(phrase.split())

    valid_words_list = [w for w in words_list if w.lower() not in stop_words_list and w.lower()]

    token_queue = Queue()
    for token in valid_words_list:
        token_queue.put(token)

def lexical(input):
   global input_string
   input_string = input
#    read_file()

   valid_alphabet = check_alphabet()

   if not(valid_alphabet):
       return False

   generate_token_queue()
   
#    global valid_words_list
#    generate_primary_symbol_table(valid_words_list)

   return token_queue.queue