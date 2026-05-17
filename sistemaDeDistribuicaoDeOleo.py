# Reservatório inicial
reservatorio = 0

# Função para abastecer o reservatório

# Cria uma função
def abastecer_reservatorio():
    # Serve para usar a mesma variavel sempre, é uma variavel global, para todas as funções.
    global reservatorio

    litros = float(input('Digite a quantidade de óleo adicionada: '))
    

    # Função acumulativa 
    
# Soma a quantidade de litros adicionadas com a quantidade que já existe no reservatorio
    reservatorio += litros

# Mostra o reservatorio atualizado
    print(f'Reservatório atualizado: {reservatorio} litros')

    
    # Função para distribuir o oleo

# Cria uma função
def distribuir_oleo():
        
    global reservatorio

    vaga = int(input('Digite o numero da vaga: '))
    quantidade = float(input('Digite a quantidade de oleo desejada: '))
        
# Verifica se há óleo suficiente no reservatorio
    if quantidade <= reservatorio:

        reservatorio -= quantidade 

        print(f'\nÓleo distribuido para a vaga {vaga}.')
        # Mostra a vaga escolhida pelo usuario

        print(f'Reservatório restante: {reservatorio} litros')
        # Mostra a quantidade restante do reservatorio
    else:
        print('\nERRO: óleo insuficiente no reservatório!')

# Função para mostar reservatório
def mostar_reservatorio():

    print(f'\nQuantidade atual no reservatório: {reservatorio} litros')
    
    # Se o reservatorio estiver com menos de cinco litros, é mostrado um alerta.
    if reservatorio <= 5:
        print('Nivel de óleo baixo.')
    elif reservatorio >= 5 and reservatorio <= 5.000:
        print('Nivel de óleo razoavel.')
    else:
        print('Nivel de óleo estavel.') 

# Adicona o item '=' 50 vezes para divisão de função. 
    print('='*50)


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
        # O 'break' encerra o sistema
    else:
        print('\nOpção inválida. Tente novamente.')


