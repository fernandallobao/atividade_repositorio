# 3. Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.
num = int(input('Informe um numero inteiro: '))
if num % 2 == 0:
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')