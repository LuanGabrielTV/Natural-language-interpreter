from symbol_table import symbol_table
from datetime import datetime
from input_language_grammar import perguntas, respostas
from output_language_grammar import relations

global output_string
output_string = []

global output_url
output_url = "https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl"

global is_translatable
is_translatable = True
# se uma pergunta tem correspondência na linguagem de saída (True),
# então todas atribuições pós-pergunta (aqui é assumido que continuam dizendo respeito à pergunta e por isso são concatenadas com AND)
# podem ser traduzidas. Se is_translatable = False, então a pergunta não tem correspondência, e todas as próximas atribuições (até que
# se encontre uma nova pergunta), são ignoradas no output.

def start_translation():
    
    i = 0

    while i < len(symbol_table):
        
        line = symbol_table[i]

        if line["rule"] in perguntas:

            if line["rule"] == perguntas[4]:
                # verifica se a pergunta é (Quais documentos foram criados entre DATAINICIAL e DATAFINAL ?). No caso dela, é preciso de duas linhas de informação
                i += 1
                add_pergunta([line, symbol_table[i]])
            else:
                add_pergunta([line])
        else:
            add_resposta(line)
        
        i += 1
    
    print('\nOUTPUT')
    print(''.join(output_string))
    print(output_url)

def add_pergunta(lines):

    global output_string, output_url, is_translatable
    
    correspondences = [r for r in relations if r["input"] == lines[0]["rule"]["content"]]

    if not correspondences:
        # a pergunta não é traduzível
        is_translatable = False

        print(lines[0]["rule"]["info"], " não é traduzivel")
        return
    else:
        is_translatable = True

    if len(output_string) != 0:
        # adiciona o (OR): mudança de contexto de pesquisa.
        output_string.append("OR")

    output_correspondent = correspondences[0]["output"]
    url_correspondent = correspondences[0]["url"] 

    if len(lines) != 1:
        # verifica se a pergunta é (Quais documentos foram criados entre DATAINICIAL e DATAFINAL ?)
        output_string.append(output_correspondent.format(lines[0]["identifier"], lines[1]["identifier"]))

        # URL
        data_inicial = lines[0]["identifier"]
        data_final = lines[1]["identifier"]

        data_inicial_object = datetime.strptime(data_inicial, "%d/%m/%Y")
        data_final_object = datetime.strptime(data_final, "%d/%m/%Y")
        
        output_url = '&'.join([output_url,url_correspondent.format(data_inicial_object.month, data_inicial_object.year, data_final_object.month, data_final_object.year)])
    else:
        line = lines[0]
        output_string.append(output_correspondent.format(line["identifier"]))
        # não existe mais qualquer pergunta traduzível, então decidi não focar na URL aqui.
        

def add_resposta(line):

    global output_string, output_url, is_translatable

    correspondences = [r for r in relations if r["input"] == line["rule"]["content"]]

    if not(is_translatable):
        # a pergunta sobre a qual essa resposta complementa não pode ser traduzida. Assim, nem essa resposta pode ser incluída no output
        return
    
    if not correspondences:
        print(line["rule"]["info"], " não é traduzivel")
        return

    if len(output_string) != 0:
        # adicionar o (AND)
        output_string.append("AND")

    output_correspondent = correspondences[0]["output"]
    url_correspondent = correspondences[0]["url"]
    output_string.append(output_correspondent.format(line["identifier"]))

    # URL
    data = line["identifier"]
    data_object = datetime.strptime(data, "%d/%m/%Y")
    output_url = '&'.join([output_url, url_correspondent.format(data_object.month, data_object.year)])
