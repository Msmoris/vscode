from datetime import date

verde = '\033[92m'
vermelho = '\033[91m'
amarelo = '\033[93m'
reset = '\033[0m'

#Nome
print( vermelho + '""""""""""Perfil""""""""""'+ reset)
nome = input('Digite seu nome: ')
print(f'Seja bem vindo, {nome}!')

#Data de nascimento
#print('\nAgora vamos adicionar sua data de aniversário.')
#dia = int(input('Digite o dia: '))
#mes = int(input('Digite o mês: '))
#ano = int(input('Digite o ano: '))

#Validação do dia:
print('\nAgora vamos adicionar sua data de aniversário.')
while True: 
    dia = int(input('Digite o dia: '))
    if dia <= 31:
        break
    else:
        print('Dia inválido! Digite um dia entre 1 e 31.')

#Validação do mês:
while True:
    mes = int(input('Digite o mês: '))
    if mes <=12:
        break
    else:
        print('Mês inválido! Digite um mês entre 1 e 12.')

#Ano:
ano = int(input('Digite o ano: '))

#Calcular Idade:
hoje = date.today()
idade = hoje.year - ano 

#Ajuste se ainda não fez aniversário esse ano:
if (mes, dia) > (hoje.month, hoje.day):
    idade -= 1

print('\n**Dados Cadastrados**')
print(f'Nome: {nome}')
print(f'Aniversário: {dia}/{mes}/{ano}')
print(f'Idade Atual: {idade} anos')


#print('\nData de Aniversário:{}/{}/{}'.format(dia, mes, ano))
    #OU print(f'\nData de Aniversário:{}/{}/{}')
#else:
#   print('Data inválida!') 


#Outra forma de capturar o nome: (Mais fácil)
#nome = input('Digite seu nome: ')
#print(f'Seja bem vindo, {nome}!') #Sem o "f" ele não reconhece a variável, e imprime o nome da variável, e não o valor dela.
#Outra forma de fazer o format no print:
#print('Seja bem vindo, {}!'.format(nome)) #ou print('Seja bem vindo, {nome}!').format(nome=nome))