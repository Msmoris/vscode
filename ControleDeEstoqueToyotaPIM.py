# Controle de Estoque - Toyota Boshoku (PIM I - 2026)

# Cria-se uma lista 

pecas = []

def cadastrar_peca():
    nome = input('Digite o nome da peça:')
    quantidade = int(input('Digite a quantidade de peças: '))

    peca = {
        'nome': nome,
        'quantidade': quantidade
    }

    pecas.append(peca) 
