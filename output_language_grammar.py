relations = [
    {
        "input": "Quais documentos foram criados entre DATAINICIAL e DATAFINAL ?",
        "output": "[E-Publication Date:({} TO {})]",
        "url": "AfterMonth={}&AfterYear={}&BeforeMonth={}&BeforeYear={}"
    },
    {
        "input": "A data inicial é DATAINICIAL",
        "output": "[E-Publication Date: ({} TO *)]",
        "url": "AfterMonth={}&AfterYear={}"
    },
    {
        "input": "A data final é DATAFINAL",
        "output": "[E-Publication Date: (* TO {})]",
        "url": "BeforeMonth={}&BeforeYear={}"
    }
]

# no_correspondences = [
#     "Qual documento no FORMATO foi modificado mais recentemente ?",
#     "Qual documento no FORMATO foi modificado há mais tempo ?",
#     "Quais documentos são maiores que TAMANHO ?",
#     "Qual documento tem nome se iniciando em SEQUÊNCIA ?",
#     "O formato é FORMATO",
#     "O tamanho é TAMANHO",
#     "A sequência é SEQUENCIA"
# ]