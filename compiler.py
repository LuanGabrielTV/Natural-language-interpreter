from lexical import lexical
from syntax import syntax
from translator import start_translation

global input_string
input_string = ''

global instruction_counter
instruction_counter = 0

def wait_for_input():
    return input('Digite aqui: ')

if __name__ == '__main__':

    print("Use 'bye' para finalizar a execução.")

    while True:
        input_string = wait_for_input()
        if input_string.lower() == 'bye':
            start_translation()
            break

        token_queue = lexical(input_string)
        if token_queue != False:
            instruction_counter += 1
            syntax(token_queue, instruction_counter)


        
