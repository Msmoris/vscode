# Reservatório inicial
reservatorio = 0

# Função para abastecer o reservatório

# Cria uma função
def abastecer_reservatorio():

    global reservatorio

    litros = float(input('Digite a quantidade de óleo adicionada: '))

    reservatorio += litros

    print(f'Reservatório atualizado: {reservatorio} litros')

    
    # Função para distribuir o oleo

    # Cria uma função
def distribuir_oleo():
        
    global reservatorio

    vaga = input('Digite o numero da vaga: ')
    quantidade = float(input('Digite a quantidade de oleo desejada: '))
        
# Verifica se há óleo suficiente no reservatorio
    if quantidade <= reservatorio:

        reservatorio -= quantidade 

        print('\nÓleo distribuido para a vaga {vaga}.')

        print(f'Reservatório restante: {reservatorio} litros')
        
    else:
        print('\nERRO: óleo insuficiente noo reservatório!')

# Função para mostar reservatório
def mostar_reservatorio():

    print(f'\nQuantidade atual no reservatório: {reservatorio} litros')

    print('='*10)


# Menu Principal

while True:

    print('\nRESERVATÓRIO DE ÓLEO')
    print('1 - Abastecer reservatório')
    print('2 - Distribuir óleo')
    print('3 - Mostrar reservatório')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        abastecer_reservatorio()

    elif opcao == '2':
        distribuir_oleo()

    elif opcao == '3':
        mostar_reservatorio()

    elif opcao == '4':
        print('\nSistema encerrado.')
        break

    else:
        print('\nOpção inválida. Tente novamente.')

        
