"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []

while True:
    print('\n--- Menu ---')
    escolha_usuario = input(f'Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ').lower()
    print('------------')

    if escolha_usuario == 's':
        print("Saindo do programa. Até mais!")
        break

    if escolha_usuario == 'i':
        os.system('cls')
        item_inserido = input('Digite o item a ser inserido: ')
        lista.append(item_inserido)
        print(f'"{item_inserido}" adicionado.')

    elif escolha_usuario == 'a':
        if not lista:
            os.system('cls')
            print("ERRO: A lista está vazia. Nada para apagar.")
            continue

        os.system('cls')
        print("Lista atual (Escolha o número):")
        for indice, nome in enumerate(lista):
            print(f'{indice}: {nome}')

        indice_str = input('Escolha o ÍNDICE (posição) para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
            print("Item apagado com sucesso.")
        except ValueError:
            print('ERRO: O índice precisa ser um número inteiro.')
        except IndexError:
            print('ERRO: Índice fora do intervalo da lista.')

    elif escolha_usuario == 'l':
        if not lista:
            os.system('cls')
            print("A lista está vazia.")
            continue
        
        os.system('cls')
        print("--- ITENS DA LISTA ---")
        for indice, nome in enumerate(lista):
            print(f'{indice}: {nome}')
        print("----------------------")

    else:
        print('ERRO: Opção inválida. Tente [i], [a], [l] ou [s].')

    