from alphabet import separators
import pandas as pd

symbol_table = []

# def generate_primary_symbol_table(valid_words_list):
    # global symbol_table
    # symbol_table = [w for w in valid_words_list if w not in separators and not w.isdigit()]

def print_table():
    global symbol_table
    print('\n', 'TABELA DE SÍMBOLOS')

    symbol_table_df = pd.DataFrame(symbol_table)
    print(symbol_table_df)
    print('\n')

def add_symbol(symbol):
    global symbol_table

    added = False
    for s in symbol_table:
        if s['type'] == symbol['type'] and s['identifier'] == symbol['identifier']:
            s['occurrences'].append(symbol['occurrences'][0])
            added = True
            break
    
    if(not(added)):
        symbol_table.append(symbol)

def get_symbol_table():
    global symbol_table
    return symbol_table

def set_symbol_table(table):
    global symbol_table
    symbol_table = table