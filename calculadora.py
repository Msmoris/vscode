
while True:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))

    op = input('Escolha a operação que deseja realizar: +, -, *, /: ')
    if op == 'sair':
        break

    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op =='*':
        resultado = n1 * n2
    elif op == '/':
        if n2 != 0:
            resultado = n1 / n2
        else:
            print('Erro: Divisão por zero não é permitida.')
            continue
    else:
        print('operação invalida')
        continue

    print(f'O resultado da operação {n1} {op} {n2} é: {resultado:.2f}')