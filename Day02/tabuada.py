#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10

tabuada do 1 
1
2
3
4
.....
---------------
tabuada do 2
1
2
3
4
.....
"""
__version__ = "0.1.0"
__author__ = "Matheus"

# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# Iterable (percorriveis)
for numero in numeros:
    print("tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("---------------")






