perguntas = [
    {
        "content": "Qual documento no FORMATO foi modificado mais recentemente ?",
        "info": ["FORMATO"],
        "complement": ["Qual o formato ? <pdf, txt ou xml>"],
        "accepts": ["\\b(?:pdf|txt|xml)\\b"],
        "followup": [0]
    },
    {
        "content": "Qual documento no FORMATO foi modificado há mais tempo ?",
        "info": ["FORMATO"],
        "complement": ["Qual o formato ? <pdf, txt ou xml>"],
        "accepts": ["\\b(?:pdf|txt|xml)\\b"],
        "followup": [0]
    },
    {
        "content": "Quais documentos são maiores que TAMANHO ?",
        "info": ["TAMANHO"],
        "complement": ["Qual o tamanho ? <número positivo de até quatro numerais>"],
        "accepts": ["^[0-9]{1,4}$"],
        "followup": [1]
    },
    {
        "content": "Qual documento tem nome se iniciando em SEQUÊNCIA ?",
        "info": ["SEQUÊNCIA"],
        "complement": ["Qual a sequência ? <string>"],
        "accepts": ["^(?!\\s*$).+"],
        "followup": [2]
    },
    {
        "content": "Quais documentos foram criados entre DATAINICIAL e DATAFINAL ?",
        "info": ["DATAINICIAL", "DATAFINAL"],
        "complement": ["Qual a data inicial ? <dd/mm/yyyy>", "Qual a data final ? <dd/mm/yyyy>"],
        "accepts": ["(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[0,1,2])\\/(19|20)\\d{2}", "(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[0,1,2])\\/(19|20)\\d{2}"],
        "followup": [3, 4]
    },
]

respostas = [
    {
        "content": "O formato é FORMATO",
        "info": "FORMATO",
        "complement": "Qual o formato ? <pdf, txt ou xml>",
        "accepts": "\\b(?:pdf|txt|xml)\\b",
    },
    {
        "content": "O tamanho é TAMANHO",
        "info": "TAMANHO",
        "complement": "Qual o tamanho ? <número positivo de até quatro numerais>",
        "accepts": "^[0-9]{1,4}$"
    },
    {
        "content": "A sequência é SEQUENCIA",
        "info": "SEQUENCIA",
        "complement": "Qual a sequência ? <string>",
        "accepts": "^(?!\\s*$).+"
    },
    {
        "content": "A data inicial é DATAINICIAL",
        "info": "DATAINICIAL",
        "complement": "Qual a data inicial ? <dd/mm/yyyy>",
        "accepts": "(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[0,1,2])\\/(19|20)\\d{2}"
    },
    {
        "content": "A data final é DATAFINAL",
        "info": "DATAFINAL",
        "complement": "Qual a data final ? <dd/mm/yyyy>",
        "accepts": "(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[0,1,2])\\/(19|20)\\d{2}"
    }
]