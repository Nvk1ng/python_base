#!/usr/bin/env python3

email_tmpl = """
Ola, %(nome)s 

Tem interesse em comprar %(produto)s?

Este produto e otimo para resolver

%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preco promocional %(preco).2f"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        %{
            "nome": cliente,
            "produto": "Caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )

