#!/usr/bin/env python

email_tmpl = """

Olá %(nome)s,

Tem interesse em comprar %(produto)s?

Este produto é otimo parar resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade) disponivel

Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bom",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
