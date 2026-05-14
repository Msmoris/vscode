# Controle de Estoque - Toyota Boshoku (PIM I - 2026)

# Cria-se uma lista 
pecas = []

def cadastrar_peca():

    nome = input('Digite o nome da peça: ').lower()
    quantidade = int(input('Digite a quantidade de peças: '))

    # Verifica se a peça já existe
    for peca in pecas:

        if peca['nome'] == nome:
            peca['quantidade'] += quantidade

            print('Quantidade atualizada com sucesso!')
            return


# Em caso da peça não existir
    nova_peca = {
        'nome':nome,
        'quantidade':quantidade
    }
    
    pecas.append(nova_peca) 
    
    print('Peça cadastrada com sucesso!')


# Função para mostrar estoque
def mostrar_estoque():

    if len(pecas) == 0:
        print('Nenhuma peça cadastrada.')

    else:
        print('\nESTOQUE DA TOYOTA')

        for peca in pecas:
            print(f"Peça: {peca['nome'].capitalize()}")
            print(f"Quantidade: {peca['quantidade']}")
           
        # Aviso de estoque baixo
            if peca ['quantidade'] < 5:
                print('Estoque baixo!')
            
            
            print('=' * 20)


# Menu principal
while True:
    print('\nSISTEMA TOYOTA')
    print('1 - Cadastrar peça')
    print('2 - Mostrar estoque')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_peca()

    elif opcao == '2':
        mostrar_estoque()

    elif opcao == '3':
        print('Sistema encerrado.')
        break

    else:
        print('Opção invalida.')          


