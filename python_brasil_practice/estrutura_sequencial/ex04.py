# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite a primeira nota bimestral:"))
nota2 = int(input("Digite a segunda nota bimestral:"))
nota3 = int(input("Digite a terceira nota bimestral:"))
nota4 = int(input("Digite a quarta nota bimestral:"))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print(f"A sua nota no primeiro bimestre foi {nota1}, no segundo foi {nota2}, no terceiro {nota3} e no quarto {nota4} e sua média final foi de {media}")
