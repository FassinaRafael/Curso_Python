def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

produtos = multiplica(2, 3, 6, 7)
print(produtos)

def par_ou_impar(valor):
    multiplo_de_dois = valor % 2 == 0

    if multiplo_de_dois:
        return f'{valor} é par'
    return f'{valor} é ímpar'

print(par_ou_impar(2))
print(par_ou_impar(5))
print(par_ou_impar(77))
print(par_ou_impar(128))