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



