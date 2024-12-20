#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente 

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:
    
    pyton3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.01"
__author__ = "Matheus Sanderhus"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG", "en_US") [:5]

msg = "Hello, World!!" 

if current_language == "pt_BR":
    msg = "Ola, Mundo!!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!!"
elif current_language == "es_SP":
    msg = "Ola, mundo!!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!!"

print(msg)


