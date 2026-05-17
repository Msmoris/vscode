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

            print('Óleo distribuido para a vaga {vaga}.')

            print(f'Reservatório restante: {reservatorio} litros')
        
        else:
            print('\nERRO: óleo insuficiente noo reservatório!')