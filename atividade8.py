# 8. Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
numeros = []
while True: 
    
    novo_numero = input('Informe um numero de 0 a 10 ou f para fechar a lista de numeros: ').lower()
    if novo_numero != 'f':
        if novo_numero >=0 and novo_numero <= 10: 
            novo_numero = int(novo_numero)
            numeros.append(novo_numero)
        else:
            print('O numero não esta dentro dos padrões!')
            continue
    else:
        break

media = sum(numeros)/len(numeros)

print(f'Resultado da media: {media:,.2f}.')     
  