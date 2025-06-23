from symbol_table import add_symbol, print_table, get_symbol_table, set_symbol_table
from lexical import lexical
from grammar import perguntas, respostas
from utils import get_strings_similarity
import re
from errors import no_mobilized_rule_error, pending_rule_error
import copy

global pending_answer
pending_answer = []

def add_symbol_in_table(type, identifier, instruction_index):
    
    print(instruction_index)

    symbol = {
        "type": type,
        "identifier": identifier,
        "occurrences": [instruction_index]
    }
    
    add_symbol(symbol)

    print_table()

def fit_into_grammar(instruction_index):
    global mobilized_rule, token_queue, pending_answer
    copied_queue_list = list(copy.copy(token_queue))
    
    if mobilized_rule in perguntas:

        if len(pending_answer) != 0:
            print(pending_rule_error.format(' '.join(str(answer["complement"]) for answer in pending_answer)))
            return 

        i = 0
        for j in range(min(len(copied_queue_list), len(mobilized_rule['content'].split()))):
            current_word = mobilized_rule['content'].split()[j]
            
            if current_word in mobilized_rule['info']:    
                k = mobilized_rule['info'].index(current_word)
                
                if mobilized_rule['content'].split()[j+1] == copied_queue_list[i]:
                    pending_answer.append(respostas[mobilized_rule['followup'][k]])
                    print(mobilized_rule['complement'][k])
                
                else:
                    pattern = re.compile(r'' + mobilized_rule['accepts'][k])
                    
                    if not(bool(pattern.match(copied_queue_list[i]))):
                        pending_answer.append(respostas[mobilized_rule['followup'][k]])
                        print(mobilized_rule['complement'][k])
                    
                    else:
                        add_symbol_in_table(mobilized_rule['info'][k], copied_queue_list[i], instruction_index)
                        
                        if len(pending_answer) != 0:
                            pending_answer.remove(respostas[mobilized_rule['followup'][k]])
                    
                    i += 1
            else:
                i += 1 
    else:

        if len(pending_answer) != 0:
            if mobilized_rule not in pending_answer:
                print(pending_rule_error.format(' '.join(str(answer["complement"]) for answer in pending_answer)))
                return

        for j in range(len(mobilized_rule['content'].split())):
            
            if j < len(copied_queue_list):
                current_word = mobilized_rule['content'].split()[j]
             
                if current_word == mobilized_rule['info']:
                    pattern = re.compile(r'' + mobilized_rule['accepts'])
                  
                    if not(bool(pattern.match(copied_queue_list[j]))):
                        print(mobilized_rule['complement'])

                    else:

                        if len(pending_answer) != 0:
                            pending_answer.remove(mobilized_rule)
                      
                        add_symbol_in_table(mobilized_rule['info'], copied_queue_list[j], instruction_index)
            else:
                pending_answer.append(mobilized_rule)
                print(mobilized_rule['complement'])

def find_mobilized_rule():
    global token_queue
    copied_queue_list = list(copy.copy(token_queue))
    possible_perguntas = perguntas.copy()
    possible_respostas = respostas.copy()

    for p in perguntas:
        i = 0
        for j in range(min(len(copied_queue_list), len(p['content'].split()))):
            current_word = p['content'].split()[j]
            if current_word not in p['info']:
                if copied_queue_list[i] != current_word:
                    possible_perguntas.remove(p)
                    break
                i += 1
            else:
                if p['content'].split()[j+1] == copied_queue_list[i]:
                    j += 1
                else:
                    i += 1

    for r in respostas:
        for j in range(min(len(copied_queue_list), len(r['content'].split()))):
            current_word = r['content'].split()[j]
            if(current_word != r['info']):
                if copied_queue_list[j] != current_word:
                    possible_respostas.remove(r)
                    break
          
    if len(possible_perguntas) != 0 or len(possible_respostas) != 0:
        return (possible_perguntas + possible_respostas)[0]
    return None

def syntax(queue, instruction_index):

    global token_queue, mobilized_rule
    token_queue = queue
    mobilized_rule = find_mobilized_rule()

    if mobilized_rule == None:
        print(no_mobilized_rule_error)
        return
    else:
        return fit_into_grammar(instruction_index)

