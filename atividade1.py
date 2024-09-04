# 1. Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.

try:
    num = float(input('Informe um numero: '))
    print(num, type(num))
except Exception as e: #mostra ums msg de erro sem interromper o programa e mostra qual foi o tipo de erro
    print(f'Não foi possivel realizar a operação! {e}')
