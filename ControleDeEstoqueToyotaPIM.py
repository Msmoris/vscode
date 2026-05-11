# Controle de Estoque - Toyota Boshoku (PIM I - 2026)

# Cria-se uma lista 

pecas = []

def cadastrar_peca():
    
    nome = input('Digite o nome da peça: ')
    quantidade = int(input('Digite a quantidade de peças: '))

    peca = {
        'nome': nome,
        'quantidade': quantidade
    }
    
    pecas.append(peca) 
    
    print('Peça cadastrada com sucesso!')

# Função para mostrar estoque
def mostrar_estoque():
    if len(pecas) == 0:
        print('Nenhuma peça cadastrada.')
    else:
        print('\nESTOQUE DA TOYOTA')

        for peca in pecas:
            print(f"Peça: {peca['nome']}")
            print(f"Quantidade: {peca['quantidade']}")
            print('-' * 20)

# Menu principal
    while True:
            print('\nSISTEMA TOYOTA')
            print('1 - Cadastrar peça')
            print('2 - Mostrar estoque')
            print('3 - Sair')

            opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_peca()
        input('Digite o nome da peça: ')
    elif opcao == '2':
        print(mostrar_estoque())
    elif opcao == '3':
        print('Sistema encerrado.')
    else:
        print('Opção invalida.')          


