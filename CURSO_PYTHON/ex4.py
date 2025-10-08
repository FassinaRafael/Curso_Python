"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input("Digite um numero inteiro: ")

try:
    numero_int = int(numero_str)
    par_impar = numero_int % 2 == 0

    if par_impar:
        print(f"O número {numero_int} é par")
    else:
        print(f"O número {numero_int} é ímpar")
except:
    print(f"{numero_str} não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite o horário atual: ")

try:
    horario_int = int(horario)
    dia = horario_int >= 0 and horario_int < 12
    tarde = horario_int >= 12 and horario_int < 18
    noite = horario_int >= 18 

    if dia:
        print("Bom dia!")
    elif tarde:
        print("Boa tarde!")
    elif noite:
        print("Boa noite!")
    else:
        print('Não conheço essa hora')

except:
    print("Insira um horário válido")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Insira seu nome: ")

try:
    tamanho_nome = len(nome)
    
    curto = tamanho_nome < 5
    normal = tamanho_nome >= 5 and tamanho_nome < 7
    longo = tamanho_nome >= 7
    
    if curto:
        print("Seu nome é curto")
    elif normal:
        print("Seu nome é normal")
    elif longo:
        print("Seu nome é longo ")
    
except:
    print("Digite um nome válido")