# print("hello world, how are you?, you guys need to meet the brazillian football team called grêmio")
# print(998-999)
# print(0+0)
# float
# x= 'qualquer coisa ai'
# print(type(x))
# respostas = {
# 'gremio':'o melhor do mundo, nao tem jeito', 'flamengo': 'se retire por favor', 'corinthians': 'minha irmã gosta,então ta de boa'
# }

# while True:
# melhortime = input("\nqual o melhor time do Brasil?: ").lower()

# if melhortime == 'sair':
# break

# if melhortime in respostas:
# print(respostas[melhortime])
# else:
# print("vaiaseferrar")

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
media = (nota1+nota2+nota3)/3
print(f"a media das notas é: {media:.2f}") #O ".2f" é para limitar a quantidade de casas decimais, nesse caso, 2.
                              