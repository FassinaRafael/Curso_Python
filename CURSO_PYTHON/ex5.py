<<<<<<< HEAD
nome = 'Rafael Fassina'
tamanho_nome = len(nome)
contador = 0

#Versão com While
while contador < tamanho_nome:
    print(f'*{nome[contador]}', end='')
    contador += 1

print('*')

#Versão com For
novo_texto = ''
for letra in nome:
    novo_texto += f'*{letra}'

=======
nome = 'Rafael Fassina'
tamanho_nome = len(nome)
contador = 0

#Versão com While
while contador < tamanho_nome:
    print(f'*{nome[contador]}', end='')
    contador += 1

print('*')

#Versão com For
novo_texto = ''
for letra in nome:
    novo_texto += f'*{letra}'

>>>>>>> master
print(novo_texto + '*')