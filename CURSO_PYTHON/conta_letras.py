# A frase original
frase = (
    'O Python é uma linguagem de programação '
    'multiparadigma. '
    'Python foi criado por Guido van Rossum.'
)

indice_atual = 0
max_ocorrencias = 0
caractere_mais_frequente = ''

while indice_atual < len(frase):
    caractere_atual = frase[indice_atual]
    
    if caractere_atual == ' ':
        indice_atual += 1
        continue

    ocorrencias_caractere_atual = frase.count(caractere_atual)

    if ocorrencias_caractere_atual > max_ocorrencias:
        max_ocorrencias = ocorrencias_caractere_atual
        caractere_mais_frequente = caractere_atual

    indice_atual += 1

print(f"Caractere mais frequente: '{caractere_mais_frequente}'")
print(f"Número de ocorrências: {max_ocorrencias}")
