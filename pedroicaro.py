# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
MediaIdade = 0
SomaIdade = 0
NomeHomemMaisVelho = ''
MaiorIdadeHomem = 0
MulheresMenorQue20 = 0
for i in range(1,5):
    nome = str(input(f"Digite o nome da {i}ª pessoa: "))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite M para MASCULINO \n F para FEMININO: \n "))
    sexo = sexo.upper()
    SomaIdade += idade
    if sexo == "M" and idade >= maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == "F" and idade < 20:
        MulheresMenorQue20 += 1
    else:
        print("Sexo invalido")
mediaIdade = SomaIdade/4
print(f'A média de idade do grupo é de {MediaIdade} anos.')
print(f'O homem mais velho tem {MaiorIdadeHomem} anos e se chama {NomeHomemMaisVelho}.')
print(f'Ao todo são {MulheresMenorQue20} mulheres com menos de 20 anos.')