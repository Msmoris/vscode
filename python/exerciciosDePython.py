# cálculo de média escolar

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))

# media = (nota1 + nota2 + nota3) / 3
# print(f'a média do aluno é: {media:.2f}')


# cálculo de salário ---------------------

# valorPhora = float(input('Digite o valor da hora trabalhada: '))
# horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
# salario = valorPhora * horasTrabalhadas * 30
# print(f'O salário do funcionário é: R${salario:.2f}')


# cálculo da área de um retangulo ---------------------

# base = float(input('digite a base do retângulo: '))
# altura = float(input('digite a altura do retangulo: '))
# area = base * altura 
# print(f'a area do retangulo é: {area:.2f}')


# cálculo de conversão de temperatura ---------------------

# celsius = float(input('Digite a temperatura em celsius: '))
# fahrenheit = 9/5 * celsius +32
# print(f'a temperatura em fahrenheit é: {fahrenheit:.2f}')


# # consumo médio de combustível ---------------------

# distancia = float(input('Digite a distância percorrida em km: '))
# combustivel = float(input('Digite a quantidade de combustível consumida em litros: '))
# consumo = distancia / combustivel
# print(f'O consumo médio de combustível é: {consumo:.2f} km/l')


# contador ---------------------

# contador = 5
# while contador >0:
#     print(contador)
#     contador -= 1


# acerte a letra ---------------------

# resp = 's'
# input('digita ae:').lower()
# while resp == 's':
#     print('ta executano carai')
#     input('tenta de novo ae: ').lower()


# calculadora de salario liquido ---------------------

ht = 40.00  #horas trabalhadas
vh = 25.00  #valor da hora
sb = ht * vh #calcula o salario bruto
if(sb>1000):
    sl = sb - (sb * 10/100) #calcula o salario liquido, descontando 10% do salario bruto
else:
    (sb<=1000)
    sl = sb - (sb * 5/100)
    print('sl = {0:.2f}'.format(sl))

# numero fatorial


# Lista while versao 2.0
# num = int(input('Digite o numero para calcular o fatorial: '))
# fat = 1
# cont = 2
# while cont <= num:
#     fat = fat * cont
#     cont = cont + 1
# print(f'o fatorial de {num} é {fat}')


# Lista 2.1 (Quantidade de notas)
soma = 0
conta = 0
while cont < 10:
    nota = float(input(f'Digite a {cont + 1} a nota:'))
    soma += nota # soma=soma+nota
    cont += 1
media = soma / 10
print(f'Soma das notas = {soma} - media - {media}')


# Lista while 2.1 ver. 1 (Quantidade de notas)
soma = 0
conta = 's'
qntdDnotas = 0
while cont == 's':
    nota = float(input(f'Digite a {qntdDnotas + 1} a nota:'))
    soma += nota # soma=soma+nota
    qntdDnotas += 1
    cont = input('Deseja continuar digitando as notas? (s/n): ').lower()
media = soma / qntdDnotas
print(f'Quantidade de notas = {qntdDnotas} - Media = {media} - Soma das notas = {soma}')


# Lista while ver. 2 (Quantidade maior de notas)
soma = 0
cont = 0
qntdDnotas = int(input(f'Digite a quantidade de notas: '))
while cont < qntdDnotas:
    nota = float(input(f'Digite a {cont + 1} a nota:'))
    soma += nota # soma=soma+nota
    cont += 1
media = soma / qntdDnotas
print(f'Quantidade de notas = {qntdDnotas} - Media = {media} - Soma das notas = {soma}')


# Numero maior
num = int(f'digite um numero maorque 0: ')
maior = 0
while num > 0:
    if num > maior:
        maior = num
    num = int(input(f'Digite um numero maior que 0: '))
print(maior)


# Numero primo
aux = 0
cont = 2
num = int(input(f'Digite um numero inteiro: '))
if num < 2:
    print(f'o numero {num} nao é primo.')
else:
    while cont < num:
        if num % cont == 0:
            aux += 1
            break
        if aux > 0:
            print(f'o numero {num} nao é primo.')
        else:
            while cont < num:
                print(f'cont - {cont}')
                break

# Numero
lista1= [1,2,3,4]
print(lista1)

# String 
lista2=['java', 'python', 'c#']
print(lista2)

# numero&string 
lista3= [1, 2, 'python', 3, 4, 'java']
print(lista3)

#Seleciona um único elemento especifico sem mencionado sua posição dentro dos colchetes
# *A CONTAGEM DE POSIÇÃO SEMPRE COMEÇA DO ZERO
lista=[1,2,3,4,5]
print(lista[0])

#Entrega o numero conforme a quantidade de numeros
lista4=[1,2,3,4,5]
print(lista4[0:2])
# Ou
lista4=[1,2,3,4,5]
print(lista4[:2]) # Ou print(lista4[2:]) -> informa os numeros depois do segundo numero
# É a mesma coisa, mas com string
lista5=['s', 'e', 'x', 't', 'a']
print(lista5[0:5])

#Altera o valor dentro da lista
lista0= [1,2,3,4,6]
lista0[4] = 5
print(lista0)

#extensão de lista
lista6=[1,2,3,4,5]
lista6.extend([6,7,8,9,10]) 
print(lista6)
lista6 += [2,5]
print(lista6)
lista6 *= 2
print(lista6)
 
#Adiciona um item na posição escolhida
lista7=['a','b','c','d']
lista7.insert(1,'p')
print(lista7)

#Remove o ultimo item da lista 
lista8=[1,2,3,4,5]
lista8.pop()
#Remove o item da posição escolhida
lista8.pop(2)
print(lista8)

#Remove o item pedido, se o item se repetir, o comando remove o primeiro que aparecer
lista9= [1,2,3,4,5]
lista9.remove(4)
print(lista9)

#Procura um item na lista, retornando se há(True) ou não(False) esse item na lista
lista10=('peixe','periquito','gato')
print('peixe-boi' in lista10)

#Informa a quantidade de itens dentro da lista
lista11= ['1,2']
print(len(lista11))
 
# Conta a quantidade de itens iguais dentro da lista, se o comando der erro ele retorna um numero inteiro (0)
lista12= [1,2,1,3,1]
print(lista12.count(1))
print(lista12.count(4))

#Localiza um item dentro da lista, se o comando der erro ele retorna uma mensagem de erro
lista13= [2,2,3,1,3]
print(lista13.index(1))


