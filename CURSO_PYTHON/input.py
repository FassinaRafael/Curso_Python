numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f"A soma dos numeros é: {int_numero_1 + int_numero_2}")

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if (primeiro_valor > segundo_valor):
    print(f"'{primeiro_valor} é maior que {segundo_valor}'")
elif (primeiro_valor < segundo_valor):
    print(f"'{primeiro_valor}' é menor que '{segundo_valor}'")
else:
    print("Os valores são iguais")