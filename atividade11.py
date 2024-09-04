# 11. Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).

def mostra_menu():
    print('1 - Calcular área do quadrilatero')
    print('2 - Calcular área do triângulo')
    print('3 - Calcular área do círculo')
    print('4 - Calcular área do trapézio')
    print('5 - Sair')


def calcular_quadrilatero(b, h):
    result = b*h
    return result

def calcular_triangulo(b, h):
    result = (b*h)/2
    return result

def calcular_circulo(r):
    result = 3.14*r**2
    return result

def calcular_trapezio(B, b, h):
    result = ((B+b)*h)/2
    return result

#progama principal
while True:
    mostra_menu()

    op = input('Escolha o numero do tipo de área que deseja calcular: ')
    match op:
        case '1':
            b = float(input('Informe a base do retângulo: ').replace(',', '.'))
            h = float(input('Informe a altura do retângulo: ').replace(',', '.'))
            print(f'A área é: {calcular_quadrilatero(b, h)}')
            continue
        case '2':
            b = float(input('Informe a base do retângulo: ').replace(',', '.'))
            h = float(input('Informe a altura do retângulo: ').replace(',', '.'))
            print(f'A área é: {calcular_triangulo(b, h)}')
            continue
        case '3':
            r = float(input('Informe o raio do círculo: ').replace(',', '.'))
            print(f'A área é: {calcular_circulo(r)}')
            continue
        case '4':
            B = float(input('Informe a base maior do trapézio: ').replace(',', '.'))
            b = float(input('Informe a base menor do trapézio: ').replace(',', '.'))
            h = float(input('Informe a altura do trapézio: ').replace(',', '.'))
            print(f'A área é: {calcular_trapezio(B, b, h)}')
            continue
        case '5':
            break
        case _:
            print('Opção inválida!')

print('Progama encerrado!')